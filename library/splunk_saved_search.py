#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Adam Miller (admiller@redhat.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: splunk_data_input_monitor
short_description: Manage Splunk Data Inputs of type Monitor
description:
  - This module allows for addition or deletion of File and Directory Monitor Data Inputs in Splunk.
version_added: "2.8"
options:
  name:
    description:
     - The file or directory path to monitor on the system.
    required: true
    type: str
  state:
    description:
      - Add or remove a data source.
    required: true
    choices: [ "present", "absent" ]

action_name defaults to the empty string.

action.<action_name>.<parameter>		Use this syntax to configure action parameters. See the following actions and parameter settings.
action.email	Boolean	The state of the email action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.
action.email.auth_password	String	The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next platform restart.
Defaults to empty string.

action.email.auth_username	String	The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string.
NOTE: Your SMTP server might reject unauthenticated emails.

action.email.bcc	String	BCC email address to use if action.email is enabled.
action.email.cc	String	CC email address to use if action.email is enabled.
action.email.command	String	The search command (or pipeline) which is responsible for executing the action.
Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.email.format	Enum	Valid values: (plain | html | raw | csv)
Specify the format of text in the email. This value also applies to any attachments.

action.email.from	String	Email address from which the email action originates.
Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf.

action.email.hostname	String	Sets the hostname used in the web link (url) sent in email actions.
This value accepts two forms:

hostname (for example, splunkserver, splunkserver.example.com)

protocol://hostname:port (for example, http://splunkserver:8000 or </code>https://splunkserver.example.com:443</code>)

When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url.

When this value begins with 'http://', it is used verbatim. NOTE: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct an externally referencable url, such as SSO environments, other proxies, or when the server hostname is not generally resolvable.

Defaults to current hostname provided by the operating system, or if that fails "localhost". When set to empty, default behavior is used.

action.email.inline	Boolean	Indicates whether the search results are contained in the body of the email.
Results can be either inline or attached to an email. See action.email.sendresults.

action.email.mailserver	String	Set the address of the MTA server to be used to send the emails.
Defaults to <LOCALHOST> or whatever is set in alert_actions.conf.

action.email.maxresults	Number	Sets the global maximum number of search results to send when email.action is enabled.
Defaults to 100.

action.email.maxtime	Number	Valid values are Integer[m|s|h|d].
Specifies the maximum amount of time the execution of an email action takes before the action is aborted. Defaults to 5m.

action.email.pdfview	String	The name of the view to deliver if sendpdf is enabled
action.email.preprocess_results	String	Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing).
Usually the preprocessing consists of filtering out unwanted internal fields.

action.email.reportCIDFontList	Enum	Space-separated list. Specifies the set (and load order) of CID fonts for handling Simplified Chinese(gb), Traditional Chinese(cns), Japanese(jp), and Korean(kor) in Integrated PDF Rendering.
If multiple fonts provide a glyph for a given character code, the glyph from the first font specified in the list is used.

To skip loading any CID fonts, specify the empty string.

Defaults to "gb cns jp kor"

action.email.reportIncludeSplunkLogo	Boolean	Indicates whether to include the Splunk logo with the report.
action.email.reportPaperOrientation	Enum	Valid values: (portrait | landscape)
Specifies the paper orientation: portrait or landscape. Defaults to portrait.

action.email.reportPaperSize	Enum	Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5)
Specifies the paper size for PDFs. Defaults to letter.

action.email.reportServerEnabled	Boolean	Not supported.
action.email.reportServerURL	String	Not supported.
For a default locally installed report server, the URL is http://localhost:8091/

action.email.sendpdf	Boolean	Indicates whether to create and send the results as a PDF. Defaults to false.
action.email.sendresults	Boolean	Indicates whether to attach the search results in the email.
Results can be either attached or inline. See action.email.inline.

action.email.subject	String	Specifies an alternate email subject.
Defaults to SplunkAlert-<savedsearchname>.

action.email.to	String	A comma or semicolon separated list of recipient email addresses. Required if this search is scheduled and the email alert action is enabled.
action.email.track_alert	Boolean	Indicates whether the execution of this action signifies a trackable alert.
action.email.ttl	Number	Valid values are Integer[p].
Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours).

If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.email.use_ssl	Boolean	Indicates whether to use SSL when communicating with the SMTP server.
Defaults to false.

action.email.use_tls	Boolean	Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls).
Defaults to false.

action.email.width_sort_columns	Boolean	Indicates whether columns should be sorted from least wide to most wide, left to right.
Only valid if format=text.

action.populate_lookup	Boolean	The state of the populate lookup action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.
action.populate_lookup.command	String	The search command (or pipeline) which is responsible for executing the action.
Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.populate_lookup.dest	String	Lookup name of path of the lookup to populate
action.populate_lookup.hostname	String	Sets the hostname used in the web link (url) sent in alert actions.
This value accepts two forms:

hostname (for example, splunkserver, splunkserver.example.com)

protocol://hostname:port (for example, http://splunkserver:8000 or https://splunkserver.example.com:443)

See action.email.hostname for details.

action.populate_lookup.maxresults	Number	Sets the maximum number of search results sent using alerts. Defaults to 100.
action.populate_lookup.maxtime	Number	Valid values are: Integer[m|s|h|d]
Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.

action.populate_lookup.track_alert	Boolean	Indicates whether the execution of this action signifies a trackable alert.
action.populate_lookup.ttl	Number	Valid values are Integer[p]
Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p.

If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.rss	Boolean	The state of the rss action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.
action.rss.command	String	The search command (or pipeline) which is responsible for executing the action.
Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.rss.hostname	String	Sets the hostname used in the web link (url) sent in alert actions.
This value accepts two forms.

hostname (for example, splunkserver, splunkserver.example.com)

protocol://hostname:port (for example, http://splunkserver:8000 or https://splunkserver.example.com:443)

See action.email.hostname for details.

action.rss.maxresults	Number	Sets the maximum number of search results sent using alerts. Defaults to 100.
action.rss.maxtime	Number	Valid values are Integer[m|s|h|d].
Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.

action.rss.track_alert	Boolean	Indicates whether the execution of this action signifies a trackable alert.
action.rss.ttl	Number	Valid values are: Integer[p]
Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).

If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.script	Boolean	The state of the script action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.
action.script.command	String	The search command (or pipeline) which is responsible for executing the action.
Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.script.filename	String	File name of the script to call. Required if script action is enabled
action.script.hostname	String	Sets the hostname used in the web link (url) sent in alert actions.
This value accepts two forms.

hostname (for example, splunkserver, splunkserver.example.com)

protocol://hostname:port (for example, http://splunkserver:8000 or https://splunkserver.example.com:443)

See action.email.hostname for details.

action.script.maxresults	Number	Sets the maximum number of search results sent using alerts. Defaults to 100.
action.script.maxtime	Number	Valid values are: Integer[m|s|h|d]
Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.

action.script.track_alert	Boolean	Indicates whether the execution of this action signifies a trackable alert.
action.script.ttl	Number	Valid values are: Integer[p]
Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 600 (10 minutes).

If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.summary_index	Boolean	The state of the summary index action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions.
Defaults to 0

action.summary_index._name	String	Specifies the name of the summary index where the results of the scheduled search are saved.
Defaults to "summary."

action.summary_index.command	String	The search command (or pipeline) which is responsible for executing the action.
Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.summary_index.hostname	String	Sets the hostname used in the web link (url) sent in summary-index alert actions.
This value accepts two forms:

hostname (for example, splunkserver, splunkserver.example.com)

protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)

See action.email.hostname for details.

action.summary_index.inline	Boolean	Determines whether to execute the summary indexing action as part of the scheduled search.
NOTE: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always).

Defaults to true

action.summary_index.maxresults	Number	Sets the maximum number of search results sent using alerts. Defaults to 100.
action.summary_index.maxtime	Number	Valid values are: Integer[m|s|h|d]
Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.

action.summary_index.track_alert	Boolean	Indicates whether the execution of this action signifies a trackable alert.
action.summary_index.ttl	Number	Valid values are: Integer[p]
Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 10p.

If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

actions	String	A comma-separated list of actions to enable.
For example: rss,email

alert.digest_mode	Boolean	Specifies whether alert actions are applied to the entire result set or on each individual result.
Defaults to 1.

alert.expires	Number	Valid values: [number][time-unit]
Sets the period of time to show the alert in the dashboard. Defaults to 24h.

Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.

alert.severity	Enum	Valid values: (1 | 2 | 3 | 4 | 5 | 6)
Sets the alert severity level.

Valid values are:

1 DEBUG 2 INFO 3 WARN (default) 4 ERROR 5 SEVERE 6 FATAL

alert.suppress	Boolean	Indicates whether alert suppression is enabled for this scheduled search.
alert.suppress.fields	String	Comma delimited list of fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled.
alert.suppress.period	Number	Valid values: [number][time-unit]
Specifies the suppresion period. Only valid if alert.supress is enabled.

Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.

alert.track	Enum	Valid values: (true | false | auto)
Specifies whether to track the actions triggered by this scheduled search.

auto - (Default) determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions.

true - force alert tracking.

false - disable alert tracking for this search.

alert_comparator	String	One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by perc
Used with alert_threshold to trigger alert actions.

alert_condition	String	Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string.
Alerts are triggered if the specified search yields a non-empty search result list.

NOTE: If you specify an alert_condition, do not set counttype, relation, or quantity.

alert_threshold	Number	Valid values are: Integer[%]
Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to "rises by perc" or "drops by perc."

alert_type	String	What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources.
allow_skew	0 | <percentage> | <duration>
Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods. Defaults to 0 (skew disabled).

This setting does not require adjusting in most use cases. Check with an admin before making any updates.

When set to a non-zero value for searches with the following cron_schedule values, the search scheduler randomly skews the second, minute, and hour on which the search runs.

    * * * * *     Every minute.
    */M * * * *   Every M minutes (M > 0).
    0 * * * *     Every hour.
    0 */H * * *   Every H hours (H > 0).
    0 0 * * *     Every day (at midnight).
When set to a non-zero value for a search that has any other cron_schedule setting, the search scheduler can randomly skew only the second on which the search runs.

The amount of skew for a specific search remains constant between edits of the search.

A value of 0 disallows skew. 0 is the default setting.

Percentage
<int> followed by % specifies the maximum amount of time to skew as a percentage of the scheduled search period.

Duration
<int><unit> specifies a maximum duration. The <unit> can be omitted only when the <int> is 0.

Valid duration units:

m
min
minute
mins
minutes
h
hr
hour
hrs
hours
d
day
days
Examples
100% (for an every-5-minute search) = 5 minutes maximum
50% (for an every-minute search) = 30 seconds maximum
5m = 5 minutes maximum
1h = 1 hour maximum
args.*	String	Wildcard argument that accepts any saved search template argument, such as args.username=foobar when the search is search $username$.
auto_summarize	Boolean	Indicates whether the scheduler should ensure that the data for this search is automatically summarized. Defaults to 0.
auto_summarize.command	String	A search template that constructs the auto summarization for this search. Defaults to
summarize override=partial timespan=$auto_summarize.timespan$ max_summary_size=$auto_summarize.max_summary_size$ max_summary_ratio=$auto_summarize.max_summary_ratio$ max_disabled_buckets=$auto_summarize.max_disabled_buckets$ max_time=$auto_summarize.max_time$ [ $search$ ]
Caution: Advanced feature. Do not change unless you understand the architecture of auto summarization of saved searches.

auto_summarize.cron_schedule	String	Cron schedule that probes and generates the summaries for this saved search.
The default value, */10 * * * * , corresponds to every ten hours.

auto_summarize.dispatch.earliest_time	String	A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time.
If this value is an absolute time, use the dispatch.time_format to format the value.

auto_summarize.dispatch.latest_time	String	A time string that specifies the latest time for summarizing this saved search. Can be a relative or absolute time.
If this value is an absolute time, use the dispatch.time_format to format the value.

auto_summarize.dispatch.time_format	String	Defines the time format used to specify the earliest and latest time. Defaults to %FT%T.%Q%:z
auto_summarize.dispatch.ttl	String	Valid values: Integer[p]
Indicates the time to live (in seconds) for the artifacts of the summarization of the scheduled search. Defaults to 60.

auto_summarize.max_disabled_buckets	Number	The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. Defaults to 2.
auto_summarize.max_summary_ratio	Number	The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Defaults to 0.1.
Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size.

auto_summarize.max_summary_size	Number	The minimum summary size, in bytes, before testing whether the summarization is helpful.
The default value, 52428800, is equivalent to 5MB.

auto_summarize.max_time	Number	Maximum time (in seconds) that the summary search is allowed to run. Defaults to 3600.
Note: This is an approximate time. The summary search stops at clean bucket boundaries.

auto_summarize.suspend_period	String	Time specfier indicating when to suspend summarization of this search if the summarization is deemed unhelpful. Defaults to 24h.
auto_summarize.timespan	String	The list of time ranges that each summarized chunk should span. This comprises the list of available granularity levels for which summaries would be available. Specify a comma delimited list of time specifiers.
For example a timechart over the last month whose granuality is at the day level should set this to 1d. If you need the same data summarized at the hour level for weekly charts, use: 1h,1d.

cron_schedule	String	Valid values: cron string
The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes.

cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43.

Schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes.

description	String	Human-readable description of this saved search. Defaults to empty string.
disabled	Boolean	Indicates if the saved search is enabled. Defaults to 0.
Disabled saved searches are not visible in Splunk Web.

dispatch.*	String	Wildcard argument that accepts any dispatch related argument.
dispatch.buckets	Number	The maximum number of timeline buckets. Defaults to 0.
dispatch.earliest_time	String	A time string that specifies the earliest time for this search. Can be a relative or absolute time.
If this value is an absolute time, use the dispatch.time_format to format the value.

dispatch.indexedRealtime	Boolean	Indicates whether to used indexed-realtime mode when doing real-time searches.
dispatch.indexedRealtimeOffset	Integer	Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.

Default for saved searches is "unset", falling back to limits.conf setting.
dispatch.indexedRealtimeMinSpan	Integer	Allows for a per-job override of the [search] indexed_realtime_default_span setting in limits.conf.

Default for saved searches is "unset", falling back to the limits.conf setting.
dispatch.latest_time	String	A time string that specifies the latest time for this saved search. Can be a relative or absolute time.
If this value is an absolute time, use the dispatch.time_format to format the value.

dispatch.lookups	Boolean	Enables or disables the lookups for this search. Defaults to 1.
dispatch.max_count	Number	The maximum number of results before finalizing the search. Defaults to 500000.
dispatch.max_time	Number	Indicates the maximum amount of time (in seconds) before finalizing the search. Defaults to 0.
dispatch.reduce_freq	Number	Specifies, in seconds, how frequently the MapReduce reduce phase runs on accumulated map values. Defaults to 10.
dispatch.rt_backfill	Boolean	Whether to back fill the real time window for this search. Parameter valid only if this is a real time search. Defaults to 0.
dispatch.rt_maximum_span	Integer
Allows for a per-job override of the [search] indexed_realtime_maximum_span setting in limits.conf.

Default for saved searches is "unset", falling back to the limits.conf setting.

dispatch.spawn_process	Boolean	Specifies whether to spawn a new search process when this saved search is executed. Defaults to 1.
Searches against indexes must run in a separate process.

dispatch.time_format	String	A time format string that defines the time format for specifying the earliest and latest time. Defaults to %FT%T.%Q%:z.
dispatch.ttl	Number	Valid values: Integer[p]. Defaults to 2p.
Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered.

If an action is triggered, the action ttl is used. If multiple actions are triggered, the maximum ttl is applied to the artifacts. To set the action ttl, refer to alert_actions.conf.spec.

If the integer is followed by the letter 'p', the ttl is interpreted as a multiple of the scheduled search period.

displayview	String	Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions.
is_scheduled	Boolean	Whether this search is to be run on a schedule
is_visible	Boolean	Specifies whether this saved search should be listed in the visible saved search list. Defaults to 1.
max_concurrent	Number	The maximum number of concurrent instances of this search the scheduler is allowed to run. Defaults to 1.
name	String	Required. A name for the search.
next_scheduled_time	String	Read-only attribute. Value ignored on POST. There are some old clients who still send this value
qualifiedSearch	String	Read-only attribute. Value ignored on POST. This value is computed during runtime.
realtime_schedule	Boolean	Controls the way the scheduler computes the next execution time of a scheduled search. Defaults to 1. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time.
If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option.

If set to 1, the scheduler might skip some execution periods to make sure that the scheduler is executing the searches running over the most recent time range.

The scheduler tries to execute searches that have realtime_schedule set to 1 before it executes searches that have continuous scheduling (realtime_schedule = 0).

request.ui_dispatch_app	String	Specifies a field used by Splunk Web to denote the app this search should be dispatched in.
request.ui_dispatch_view	String	Specifies a field used by Splunk Web to denote the view this search should be displayed in.
restart_on_searchpeer_add	Boolean	Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Defaults to 1.
Note: The peer can be a newly added peer or a peer down and now available.

run_on_startup	Boolean	Indicates whether this search runs on startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0.
Set run_on_startup to true for scheduled searches that populate lookup tables.

schedule_window	Number or auto	Time window (in minutes) during which the search has lower priority. Defaults to 0. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period.

Set to auto to let the scheduler determine the optimal window value automatically. Requires the edit_search_schedule_window capability to override auto.
search	String	Required. The search to save.
vsid	String	Defines the viewstate id associated with the UI view listed in 'displayview'.
Must match up to a stanza in viewstates.conf.

NOTES:
  - action.<action_name>	<action_name> is a string.
    The value for this setting is boolean. Use [0 | 1] .
    Enable or disable an alert action. See alert_actions.conf for available alert action types.

author: "Ansible Security Automation Team (https://github.com/ansible-security)
'''

EXAMPLES = '''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text

from ansible.module_utils.urls import Request
from ansible.module_utils.six.moves.urllib.parse import urlencode, quote_plus
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.splunk import SplunkRequest, parse_splunk_args

import copy

def main():

    argspec = dict(
        name=dict(required=True, type='str'),
        state=dict(choices=['present', 'absent'], required=True),
        blacklist=dict(required=False, type='str', default=None),
        check_indexed=dict(required=False, type='bool', default=None),
        check_path=dict(required=False, type='bool', default=None),
        crc_salt=dict(required=False, type='str', default=None),
        disabled=dict(required=False, type='str', default=None),
        followTail=dict(required=False, type='str', default=None),
        host=dict(required=False, type='str', default=None),
        host_segment=dict(required=False, type='int', default=None),
        host_regex=dict(required=False, type='int', default=None),
        ignore_older_than=dict(required=False, type='str', default=None),
        index=dict(required=False, type='str', default=None),
        recursive=dict(required=False, type='str', default=None),
        rename_source=dict(required=False, type='str', default=None),
        sourcetype=dict(required=False, type='str', default=None),
        time_before_close=dict(required=False, type='int', default=None),
        whitelist=dict(required=False, type='str', default=None),
    )

    module = AnsibleModule(
        argument_spec=argspec,
        supports_check_mode=True
    )

    # map of keys for the splunk REST API that aren't pythonic so we have to
    # handle the substitutes
    keymap = {
        'check_index': 'check-index',
        'check_path': 'check-path',
        'crc_salt': 'crc-salt',
        'ignore_older_than': 'ignore-older-than',
        'rename_source': 'rename-source',
        'time_before_close': 'time-before-close'

    }

    splunk_request = SplunkRequest(
        module,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        keymap=keymap,
        not_rest_data_keys=['state']
    )
    # This is where the splunk_* args are processed
    request_data = splunk_request.get_data()

    try:
        query_dict = splunk_request.get_by_path('servicesNS/nobody/search/data/inputs/monitor/{0}'.format(quote_plus(module.params['name'])))
    except HTTPError as e:
        # the data monitor doesn't exist
        query_dict = {}


    if module.params['state'] == 'present':
        if query_dict:
            needs_change = False
            for arg in request_data:
                if arg in query_dict['entry'][0]['content']:
                    if to_text(query_dict['entry'][0]['content'][arg]) != to_text(request_data[arg]):
                        needs_change = True
            if not needs_change:
                module.exit_json(changed=False, msg="Nothing to do.", splunk_data=query_dict)
            if module.check_mode and needs_change:
                module.exit_json(changed=True, msg="A change would have been made if not in check mode.", splunk_data=query_dict)
            if needs_change:
                splunk_data = splunk_request.create_update(
                    'servicesNS/nobody/search/data/inputs/monitor/{0}'.format(
                        quote_plus(module.params['name'])
                    )
                )
                module.exit_json(changed=True, msg="{0} updated.", splunk_data=splunk_data)
        else:
            # Create it
            _data = splunk_request.get_data()
            _data['name'] = module.params['name']
            splunk_data = splunk_request.create_update('servicesNS/nobody/search/data/inputs/monitor', data=urlencode(_data))
            module.exit_json(changed=True, msg="{0} created.", splunk_data=splunk_data)

    if module.params['state'] == 'absent':
        if query_dict:
            splunk_data = splunk_request.delete_by_path('servicesNS/nobody/search/data/inputs/monitor/{0}'.format(quote_plus(module.params['name'])))
            module.exit_json(changed=True, msg="Deleted {0}.".format(module.params['name']), splunk_data=splunk_data)

    module.exit_json(changed=False, msg="Nothing to do.", splunk_data=query_dict)

if __name__ == '__main__':
    main()
