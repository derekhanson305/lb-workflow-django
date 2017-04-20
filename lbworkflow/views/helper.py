import importlib

from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from lbworkflow import settings
from lbworkflow.models import WorkItem


def import_wf_views(wf_code, view_module_name='views'):
    wf_module = settings.WF_APPS.get(wf_code)
    return importlib.import_module('%s.%s' % (wf_module, view_module_name))


def add_processed_message(request, process_instance, act_descn='Processed'):
    messages.info(
        request,
        'Process "%s" has been %s. Current status："%s" Current user："%s"' %
        (
            process_instance.no, act_descn, process_instance.cur_activity.name,
            process_instance.get_operators_display()
        )
    )


def user_wf_info_as_dict(wf_obj, user):
    ctx = {}
    if user.is_anonymous:
        return ctx
    instance = wf_obj.pinstance
    is_wf_admin = instance.is_wf_admin(user)
    in_process = instance.cur_activity.status == 'in progress'
    workitems = WorkItem.objects.filter(
        Q(user=user) | Q(agent_user=user),
        instance=instance, status='in progress')
    workitem = workitems.first()
    transitions = []
    if workitems.exists():
        workitems.filter(receive_on=None).update(receive_on=timezone.now())
        transitions = instance.get_transitions()
    ctx['wf_code'] = instance.process.code
    ctx['process'] = instance.process
    ctx['process_instance'] = instance
    ctx['object'] = object
    ctx['workitem'] = workitem
    ctx['wf_history'] = instance.event_set.all().order_by('-created_on', '-pk')
    ctx['operators_display'] = instance.get_operators_display()
    ctx['is_wf_admin'] = is_wf_admin
    ctx['can_assign'] = in_process and (workitem or is_wf_admin or user.is_superuser)
    ctx['can_remind'] = in_process and (instance.created_by == user or is_wf_admin)
    ctx['can_give_up'] = instance.can_give_up(user)
    can_edit = (instance.cur_activity.status not in ['in progress', 'completed'] and instance.created_by == user)
    can_edit = can_edit or (instance.cur_activity.can_edit and workitem)
    can_edit = can_edit or is_wf_admin
    ctx['can_edit'] = can_edit
    ctx['can_audit'] = instance.get_todo_workitem(user)
    ctx['can_rollback'] = instance.can_rollback(user)
    ctx['transitions'] = transitions
    ctx['agree_transitions'] = instance.get_merged_agree_transitions()
    ctx['other_transitions'] = [e for e in transitions if not e.is_agree]
    # TODO add reject,given up to other_transitions?
    return ctx
