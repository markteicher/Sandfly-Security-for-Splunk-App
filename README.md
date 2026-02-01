# Sandfly Security for Splunk App

## Overview

Sandfly Security is an agentless intrusion detection and incident response platform for Linux. 

Sandfly Security automatically analyzes Linux hosts for intruders 24 hours a day without loading any software on endpoints. 

Sandfly Security retrieves security, hardware, operating system, and related system data from Linux hosts and makes this data available for analysis. Sandfly operates across virtually all Linux distributions immediately and is designed to function without introducing risk to system stability or performance.

The Sandfly Security for Splunk App is a single Splunk application that ingests events from a Sandfly Security server using the Sandfly Security REST API. The app ingests data into a user-specified Splunk index and assigns the correct sourcetype to each event. All events are ingested in JSON format to preserve the original structure and content of the Sandfly data.

The Splunk app provides dashboards, reports, and search logic for analyzing data ingested from a Sandfly Security server. 

This includes Sandfly Security alarms, suspicious activity results, SSH Hunter data, host inventory, and Sandfly server audit and error logs. 

Data retrieved by Sandfly Securitu can also be used by Splunk users to build searches, reports, anomaly detection models, and incident response workflows within Splunk.

The Splunk App is intended to surface Sandfly data directly inside Splunk so that Asset Owners and operational teams can view, analyze and action Sandfly Security results without requiring access to the Sandfly Security user interface.

## Supporting Operating Systems



⚠️ Disclaimer

These tools are not official Sandfly Security products or utilities

Use of this software is not covered by any license, warranty, or support agreement you may have with Sandfly
Security.

---

## Features

### 🛡️ Core Capabilities

| Feature | Description |
|--------|-------------|
| 🚨 Security Alarms | Pass, alert, and error results from enabled Sandflies |
| 🖥️ Host Inventory | Hosts managed by the Sandfly Server |
| 🌐 Sandflies | Active Sandflies managed by the Sandfly Server |
| 🔑 SSH Hunter Data | SSH keys, users, hosts, and zones |
| 📋 Audit Logs | Sandfly Server system audit logs |
| ❗ Error Logs | Sandfly Server scanning and operational error logs |

### 📈 Analysis and Usage

| Feature | Description |
|--------|-------------|
| 📊 Dashboards | Visual analysis of Sandfly alarms and activity |
| 🔍 Suspicious Activity Review | Review of Sandfly-detected activity |
| 🧩 Splunk Search | Use Sandfly data in custom Splunk searches |
| 🧠 Anomaly Detection | Build anomaly detection models using Sandfly data |
| ⚙️ Incident Response | Support investigations using Sandfly events |

---

## Data Ingestion

The Sandfly Security for Splunk App retrieves data from a Sandfly Security server using the Sandfly Security REST API.

Data is ingested into a Splunk index specified during configuration. Each dataset retrieved from the Sandfly server is assigned a predefined sourcetype by the app. Events are stored in Splunk as JSON-formatted data.

---

## Server Connection Requirements

To ingest events from a Sandfly Security server, the following configuration items are required:

1. Sandfly Server URL  
2. Login Username  
3. Login Password  

These credentials are used to authenticate REST API requests to the Sandfly Security server.

---

## Supported Sourcetypes

The following sourcetypes are supported and assigned by the app:

| Sourcetype | Description |
|-----------|-------------|
| sandfly:alarms | Sandfly alarms including pass, alert, and error results |
| sandfly:hosts | Hosts managed by the Sandfly Server |
| sandfly:sandflies | Active Sandflies managed by the Sandfly Server |
| sandfly:ssh:keys | SSH Hunter keys, users, hosts, and zones |
| sandfly:logs:audit | Sandfly Server audit logs |
| sandfly:logs:error | Sandfly Server error and scanning logs |

---

## Dashboards

| Dashboard | Description |
|----------|-------------|
| 🧭 Overview | Summary of Sandfly activity and metrics |
| 🚨 Alarms | Sandfly alarm results |
| 🖥️ Hosts | Linux host inventory |
| 🔑 SSH Keys | SSH Hunter analysis |
| 📈 Metrics | Software and hardware metrics |
| 📋 Logs | Audit and error log visibility |

---

## Installation

### Step 1: Install the App

1. Download the Sandfly Security for Splunk App package  
2. In Splunk Web, navigate to Apps → Manage Apps  
3. Select Install app from file  
4. Upload the application package  
5. Restart Splunk if prompted  

---

### Step 2: Configure the App

1. Navigate to Apps → Sandfly Security → Setup  
2. Enter the Sandfly Server URL  
3. Enter the login username and password  
4. Select the target Splunk index for data ingestion  

---

### Step 3: Verify Data Collection

Run the following search to confirm data ingestion:

    index=<your_index> sourcetype=sandfly:*
    | stats count by sourcetype

---

## App Structure

Sandfly_Security_For_Splunk_App/
  app.manifest
  LICENSE
  README.md
  default/
    app.conf
    inputs.conf
    indexes.conf
    props.conf
    transforms.conf
    savedsearches.conf
    data/ui/
      nav/
      views/
  bin/
  metadata/
  static/

---

## Requirements

- Splunk Enterprise or Splunk Cloud
- Network connectivity to a Sandfly Security server
- Valid Sandfly Security credentials
- Sandfly Security platform deployed and operational

---

## Reference

- Sandfly Security product documentation
- Sandfly Security REST API documentation
- Splunk documentation: https://docs.splunk.com

---

## License

Refer to the application package for licensing information.
