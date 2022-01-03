**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation
TODO: run kubectl command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

x-special/nautilus-clipboard
copy
file:///home/fadwa/Apps/phase2/obs/observability/dashboard/answer-img/1.%20monitoring%20all.png

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

## Describe SLO/SLI
Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

99% uptime of system per month.(all HTTP statuses will be 20x).
99% of all requests will take less than 20ms in a given month (responce time).

if we have these SLOs the SLIs should be metrics to measure  those SLOs (the level of performance) in a given time. It is ratio x/y (x: performance, y: specific time )

Ex:
-The average time taken to return a request during the month was 11 ms. (responce time).
-The rate of errors per month was 5%. 


## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

# 5 metrics 
1. average responce time per minute : to know how fast of system replaying to requests.
2. No. of error per month : to know where the problem of system.
3. No. of requests per seconed: to know the traffic and where  bottleneck can happen.
4. CPU useage : to know how saturation of the system.
5. Meomery useage : to know how the system consume the resources. 


## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

*TROUBLE TICKET 1

Name:trial/trace error

Date: 3 Jan 2022

Subject: JosnDecodeError

Affected Area: trial/app/app.py

Severity: high

Description: raise JSONDecodeError("Expecting value", s, err.value) from None



*TROUBLE TICKET 2

Name:trial/homepage error

Date: 3 Jan 2022

Subject: 500 internal error

Affected Area: trial/app/app.py

Severity: high

Description: couldn't find main template 


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

we will use four golden metrics to insure our system is uptime 99.95% per month\
1. latancy
2. saturation
3. traffic
4. errors


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.


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
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

