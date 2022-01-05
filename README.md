**Cloud Native Observability:** 
This project create dashboards that use multiple graphs to monitor the sample application that is deployed on a Kubernetes cluster. 
The project use Prometheus, Jaeger, and Grafana in order to monitor, trace and visualize the application. 


## 1- Verify the monitoring installation
 screenshot to verify the installation shows the running pods and services for all components.

![1  monitoring all](https://user-images.githubusercontent.com/24944117/148044196-255e06b5-7ed0-40fb-a26b-49635d4c2753.png)

## Setup the Jaeger and Prometheus source
Expose Grafana to the internet and then setup Prometheus as a data source. The screenshot of the home page after logging into Grafana.

![2  grafana home](https://user-images.githubusercontent.com/24944117/147992783-91031eab-380c-439f-91e3-15956f2edf4b.png)

## Create a Basic Dashboard
 Screenshot show dashboard in Grafana and use Prometheus as a source.
![3  prometheus datasource](https://user-images.githubusercontent.com/24944117/147992955-d4c58205-eb96-401e-b5f6-bc18e3cbdce6.png)

## Describe SLO/SLI
*Describtion  what the SLIs are, based on an SLO of *monthly uptime* and *request response time**.

99% uptime of system per month.(all HTTP statuses will be 20x).
99% of all requests will take less than 20ms in a given month (responce time).

if we have these SLOs the SLIs should be metrics to measure  those SLOs (the level of performance) in a given time. 
It is ratio x/y (x: performance, y: specific time )

Ex:
-The average time taken to return a request during the month was 11 ms. (responce time).
-The rate of errors per month was 5%. 


## Creating SLI metrics.
 It is important to know why we want to measure certain metrics for our customer. Describtion in detail 5 metrics to measure these SLIs. 

*5 metrics* 
1. average responce time per minute : to know how fast of system replaying to requests.
2. No. of error per month : to know where the problem of system.
3. No. of requests per seconed: to know the traffic and where  bottleneck can happen.
4. CPU useage : to know how saturation of the system.
5. Meomery useage : to know how the system consume the resources. 


## Create a Dashboard to measure our SLIs
A dashboard to measure the uptime of the frontend and backend services,also  measure 40x and 50x errors. A screenshot for dashboard that show these values over a 24 hour period.

![4  SLIs](https://user-images.githubusercontent.com/24944117/147993035-6964450d-2a88-4ed0-a1b8-1e050d696dd9.png)


## Tracing our Flask App
 create a Jaeger span to measure the processes on the backend and fill in the span,  the screenshot show backend span use Jaeger. 

![5  backend jaeger](https://user-images.githubusercontent.com/24944117/147993081-dda213f3-7707-4815-a5dd-a026734d239c.png)

screenshot show sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

![6  backend tracing code](https://user-images.githubusercontent.com/24944117/147993084-a84e0bf4-ed13-4017-a9cb-beebb9ff9f59.png)

## Jaeger in Dashboards
Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed,  a screenshot to show it.
![7  backend traincing dashboard](https://user-images.githubusercontent.com/24944117/147993090-c468da4d-23d9-4893-ad91-7cd41e3d8b91.png)

## Report Error
The trouble ticket for the developers, to explain the errors appear in code (400, 500, latency) with file that is causing the issue.and the screenshut show  the tracer span to demonstrate how a tracer use to locate errors easily.

*TROUBLE TICKET 1*

Name:trial/trace error

Date: 3 Jan 2022

Subject: JosnDecodeError

Affected Area: trial/app/app.py

Severity: high

Description: raise JSONDecodeError("Expecting value", s, err.value) from None

![8  trial ticket](https://user-images.githubusercontent.com/24944117/147993095-949221c9-f721-4e1e-a45f-baecdbebeccd.png)

*TROUBLE TICKET 2*

Name:trial/homepage error

Date: 3 Jan 2022

Subject: 500 internal error

Affected Area: trial/app/app.py

Severity: high

Description: couldn't find main template 

![9  homepage ticket](https://user-images.githubusercontent.com/24944117/147993096-7176b032-d9bd-4b2f-9eb9-7a1ba6ca8e99.png)

## Creating SLIs and SLOs
  create an SLO guaranteeing that our application has a *99.95% uptime per month*. with four SLIs that  would use to measure the success of this SLO.

 useing four golden metrics to insure our system is uptime 99.95% per month

SLIs:
1. latancy: 95% of requests responce under 1 minute
2. saturation: resources usage not exceed 70 % (meomery & CPU)
3. traffic: no of successful requests per minute
4. errors: errors not exceeds 0.05% per month 


## Building KPIs for our plan
After SLIs and SLOs, this a  list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs was chosen. Screenshut show dashboard for this.

A. latancy 
1. no of traces , to know latacncy whitch affect system uptime
2. average resonce time :to calculate time need for request to get replay
3. request under 250ms : to ensure the sysytem is up and work pefectly

B. saturation
1. CPU Usage : to monitor need of cpu by system helping in optimal usage of resources
2. Meomery Usage : to know how much resources need to make system up all the month

c. traffic 
1. no of requests per minute : to know the bandwidth you need for system to be up
2. Request duration : to know how much time the request need to get responce

d. errors
1. no of errors per second : to know how much bugs affect the system
2. 5X and 4x errors : to know area of defect in system hepling in solve it to prevent any attack to system to ensure the system secure and available all time. 


## Final Dashboard
 Final Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. The screenshot show the final dashboard, with text description of what graphs are represented in the dashboard.  

![final dashboard 1](https://user-images.githubusercontent.com/24944117/148044203-6b942a03-9715-407e-bcb2-860deeba0a49.png)

![final dashboard 2](https://user-images.githubusercontent.com/24944117/148044207-47578ccf-4662-4a78-a5d1-27973d6a09b1.png)

