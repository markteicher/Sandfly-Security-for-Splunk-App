<!--
=============================================================================
 default/data/ui/views/sandfly_users_audit_log.xml
 Sandfly Security for Splunk App
 Users — Audit Log
=============================================================================

PURPOSE

Displays a chronological audit-style view of Sandfly user activity derived
from /v4/users ingestion.

This view answers:

- Who logged in?
- When did they last log in?
- From where?
- Which users are active vs dormant?
- What roles and auth methods were in use at the time?

DATA SOURCE

- /v4/users  → sourcetype=sandfly:users

Expected fields:
  username
  email
  full_name
  roles
  sso
  last_login_date
  last_login_ip
  created_date

NOTES

- This is an activity/audit view, not an access governance dashboard.
- All timestamps are rendered directly from ingested fields.
- No inferred risk scoring.
=============================================================================
-->

<dashboard version="1.1" theme="light">
  <label>Users — Audit Log</label>

  <description>
    Chronological audit view of Sandfly user activity based on /v4/users ingestion.
  </description>

  <row>
    <panel>
      <title>👤 User Activity Audit Log</title>
      <table>
        <search>
          <query>
            index=* sourcetype=sandfly:users earliest=0
            | spath
            | eval last_login_epoch=case(
                isnull(last_login_date) OR last_login_date="",
                null(),
                1=1, strptime(last_login_date,"%Y-%m-%dT%H:%M:%S.%3NZ")
              )
            | eval days_since_login=if(
                isnull(last_login_epoch),
                null(),
                round((now()-last_login_epoch)/86400,0)
              )
            | table
                username
                email
                full_name
                roles
                sso
                last_login_date
                last_login_ip
                days_since_login
                created_date
            | sort - last_login_epoch
          </query>
        </search>

        <option name="wrap">true</option>
        <option name="rowNumbers">false</option>
        <option name="count">50</option>
      </table>
    </panel>
  </row>

</dashboard>
