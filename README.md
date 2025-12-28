# AWS Cost Optimization Tool

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900.svg)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PowerShell](https://img.shields.io/badge/PowerShell-7.0+-5391FE.svg?logo=powershell&logoColor=white)](https://github.com/PowerShell/PowerShell)
[![FinOps](https://img.shields.io/badge/Type-FinOps-success.svg)]()

> **Automated AWS cost analysis and optimization tool—identify waste, get actionable recommendations, and reduce cloud spending by 15-30%**

---

## 🎯 TL;DR

**What:** PowerShell and Python-based utility that analyzes your AWS account, identifies underutilized resources, generates cost reports, and provides specific recommendations to reduce cloud spending.

**Why:** Cloud costs spiral without visibility and automation. This tool automatically finds idle EC2 instances, unattached EBS volumes, old snapshots, and other waste—then tells you exactly how much you can save.

**Skills:** AWS Cost Explorer API • boto3 automation • PowerShell scripting • FinOps practices • Resource optimization • Cost reporting • Data analysis

**Savings Potential:** Typical findings: 15-30% cost reduction through automated waste identification

**For Roles:** Cloud Cost Analyst • FinOps Engineer • Cloud Operations • AWS Support • DevOps Engineer • Cloud Architect

---

## 📊 What This Tool Does

### Automated Cost Analysis

| Feature | Description | Savings Potential |
|---------|-------------|-------------------|
| **Idle EC2 Instances** | Finds instances with < 5% CPU for 7+ days | 20-40% of EC2 costs |
| **Unattached EBS Volumes** | Identifies volumes not attached to instances | $5-50 per volume/month |
| **Old Snapshots** | Detects snapshots older than 90 days | 10-20% of storage costs |
| **Underutilized RDS** | Finds databases with low connections | 30-50% of RDS costs |
| **Elastic IPs** | Detects unattached Elastic IPs | $3.60 per IP/month |
| **Old Load Balancers** | Identifies ALB/NLB with no traffic | $16-22 per LB/month |

### Cost Reports Generated

```
Monthly Reports Include:
├── Executive Summary (total spend, trends, top 3 savings)
├── Resource Breakdown (by service, by region)
├── Waste Analysis (idle resources, estimated savings)
├── Recommendations (prioritized action items)
├── Trend Analysis (month-over-month comparison)
└── Detailed CSV Export (for further analysis)
```

---

## 🚨 Cost Optimization Scenarios

Real-world cost incidents this tool helps prevent and resolve:

### Scenario 1: The Forgotten Test Environment

**Incident Report:**
```
Priority: Medium
Impact: $1,200/month waste
Problem: Staging environment left running after project completion
Duration: 3 months unnoticed
```

**Investigation:**
```bash
# Tool automatically detected the waste
python cost_analyzer.py --filter-tags Environment=staging

# Findings:
✓ 15 EC2 instances with < 2% CPU for 90+ days
✓ All instances tagged "staging"  
✓ Last deployment: 90 days ago
✓ No recent SSH/RDP connections
```

**Root Cause:**
- Test environment spun up for Q3 product launch
- Project completed, team forgot to tear down infrastructure
- No auto-shutdown policy configured

**Resolution:**
- Stopped all 15 idle EC2 instances
- Implemented auto-shutdown tags for non-prod environments
- Created CloudWatch alarm for idle staging resources

**Savings:** $1,200/month ($14,400/year)

**Prevention:**
- Set up automated cost anomaly detection
- Enforce resource tagging policy
- Implement scheduled auto-shutdown for dev/test environments

---

### Scenario 2: Snapshot Accumulation Crisis

**Incident Report:**
```
Priority: High
Impact: $450/month in snapshot costs (was $50)
Problem: EBS snapshot costs grew 900% in 8 months
Duration: Unnoticed for 8 months
```

**Investigation:**
```bash
# Analyze snapshot age and cost
python cost_analyzer.py --resources snapshots --older-than 90

# Findings:
✓ 240 total snapshots
✓ 180 snapshots older than 90 days
✓ 45 snapshots older than 180 days
✓ 12 orphaned snapshots (original volumes deleted)
```

**Root Cause:**
- Daily automated backups configured
- No lifecycle policy to delete old snapshots
- Snapshots kept indefinitely
- Backup volumes deleted but snapshots remained

**Resolution:**
- Deleted 180 snapshots older than 90 days (after verification)
- Implemented lifecycle policy: keep 7 daily, 4 weekly, 3 monthly
- Created Lambda function to clean up orphaned snapshots

**Savings:** $350/month ($4,200/year)

**Prevention:**
- Automated snapshot lifecycle management
- Monthly orphaned resource cleanup
- Dashboard tracking snapshot growth

---

### Scenario 3: Over-Provisioned RDS Database

**Incident Report:**
```
Priority: High
Impact: $600/month waste
Problem: Production database sized for peak load that never occurred
Duration: 6 months over-provisioned
```

**Investigation:**
```bash
# Analyze RDS utilization
python cost_analyzer.py --resources rds --detailed-metrics

# Findings:
✓ db.r5.4xlarge instance: $800/month
✓ CPU utilization: avg 5%, max 12%
✓ Connections: avg 8/day (capacity for 1000+)
✓ Memory: using 15% of available
```

**Root Cause:**
- Database sized for anticipated traffic spike
- Spike never materialized
- No review process for right-sizing

**Resolution:**
- Tested workload on db.r5.xlarge (4x smaller)
- Performed maintenance window migration
- Monitored performance post-downsize (no degradation)

**Savings:** $600/month ($7,200/year)

**Prevention:**
- Quarterly right-sizing review
- CloudWatch alarms for utilization thresholds
- Auto-scaling for RDS Aurora (when applicable)

---

### Scenario 4: Idle Load Balancer Graveyard

**Incident Report:**
```
Priority: Medium
Impact: $150/month waste
Problem: Load balancers left running for decommissioned applications
Duration: 4-8 months per LB
```

**Investigation:**
```bash
# Find load balancers with no traffic
python cost_analyzer.py --resources elb --no-traffic-days 30

# Findings:
✓ 7 Application Load Balancers found
✓ 0 requests in last 30 days for all
✓ Associated targets all unhealthy/deregistered
✓ ALB age: 4-8 months
```

**Root Cause:**
- Applications migrated to new infrastructure
- Old ALBs not deleted during migration
- No process to identify unused load balancers

**Resolution:**
- Verified with app teams (all apps migrated)
- Deleted 7 unused load balancers
- Documented decommissioning checklist

**Savings:** $150/month ($1,800/year)

**Prevention:**
- Monthly load balancer audit
- Automated alerts for LBs with no traffic
- Mandatory resource cleanup in migration runbooks

---

### Scenario 5: Unattached Elastic IP Epidemic

**Incident Report:**
```
Priority: Low
Impact: $50/month waste
Problem: Elastic IPs reserved but not in use
Duration: 2-6 months per IP
```

**Investigation:**
```bash
# Find unattached Elastic IPs
python cost_analyzer.py --resources eip --unattached

# Findings:
✓ 14 unattached Elastic IPs
✓ Cost: $3.60/month each = $50.40/month total
✓ Idle for 60+ days
✓ Associated instances terminated
```

**Root Cause:**
- Instances terminated without releasing EIPs
- Manual IP management without cleanup process
- No alerting for unattached IPs

**Resolution:**
- Released all 14 unattached Elastic IPs
- Documented which IPs were truly needed (reserved)
- Created process for IP lifecycle management

**Savings:** $50/month ($600/year)

**Prevention:**
- Weekly unattached EIP scan
- Automated release after 7 days unattached
- Use ALB/NLB instead of Elastic IPs where possible

---

### Scenario 6: CloudWatch Logs Explosion

**Incident Report:**
```
Priority: High
Impact: $280/month waste
Problem: CloudWatch Logs costs jumped from $20 to $300/month
Duration: 2 weeks of excessive logging
```

**Investigation:**
```bash
# Analyze log group sizes and ingestion
python cost_analyzer.py --resources cloudwatch-logs --size-threshold 10GB

# Findings:
✓ Application log group: 50 GB/day ingestion
✓ Retention: Never expire
✓ Log level: DEBUG in production
✓ Cost: $0.50/GB = $750/month projected
```

**Root Cause:**
- Developer enabled DEBUG logging to troubleshoot issue
- Forgot to revert to INFO level after fix
- No alerting on log ingestion spikes

**Resolution:**
- Changed log level to INFO (reduced ingestion by 90%)
- Set retention to 30 days for application logs
- Implemented log level management automation

**Savings:** $280/month ($3,360/year)

**Prevention:**
- CloudWatch alarm for log ingestion spikes
- Automated log level enforcement
- Regular review of log retention policies

---

### Scenario 7: After-Hours Auto Scaling Waste

**Incident Report:**
```
Priority: Medium
Impact: $600/month waste
Problem: Auto Scaling configured for business hours 24/7
Duration: Ongoing for 4 months
```

**Investigation:**
```bash
# Analyze usage patterns
python cost_analyzer.py --analyze-usage-patterns --resource ec2

# Findings:
✓ Business hours (8am-6pm M-F): 20 instances needed
✓ After hours + weekends: Only 5 instances needed
✓ Current setup: Min 20, Max 30 instances (always)
✓ 70% capacity idle during off-peak (126 hrs/week)
```

**Root Cause:**
- Auto Scaling Group configured for peak load 24/7
- No schedule-based scaling policies
- Assumed always needed maximum capacity

**Resolution:**
- Implemented scheduled scaling:
  - Business hours: Min 20, Max 30
  - After hours: Min 5, Max 10
  - Weekends: Min 3, Max 8
- Monitored for 2 weeks (no performance impact)

**Savings:** $600/month ($7,200/year)

**Prevention:**
- Analyze usage patterns quarterly
- Implement predictive scaling where applicable
- Regular review of auto-scaling policies

---

## 💡 Skills Demonstrated

### ☁️ Cloud Financial Management (FinOps)

| Skill | Implementation | Business Value |
|-------|----------------|----------------|
| **Cost Visibility** | Multi-region resource scanning, aggregation, reporting | Identify all cloud spending |
| **Cost Allocation** | Tag-based tracking, team attribution | Accountability per team/project |
| **Waste Identification** | Automated detection of idle/unused resources | Immediate savings opportunities |
| **Right-Sizing** | Usage analysis, recommendations | 20-40% compute cost reduction |
| **Forecasting** | Trend analysis, budget prediction | Accurate budget planning |
| **Governance** | Policy enforcement, compliance checks | Prevent future waste |
| **Optimization** | Savings Plans, Reserved Instances analysis | Long-term cost reduction |

### 🐍 Python Development

```
✓ AWS boto3 SDK automation
✓ Multi-threaded resource scanning (concurrent.futures)
✓ Object-oriented design patterns
✓ Data processing with pandas and numpy
✓ HTML/CSV/JSON report generation
✓ Advanced error handling and logging
✓ Configuration management (YAML, JSON)
✓ Unit testing with pytest
✓ API rate limiting and pagination
✓ Asynchronous programming (asyncio)
```

### 💻 PowerShell Scripting

```
✓ AWS PowerShell module (AWSPowerShell.NetCore)
✓ Pipeline-oriented programming
✓ Advanced parameter validation
✓ Object manipulation and filtering
✓ Module development and distribution
✓ Progress bars and user feedback
✓ Export to multiple formats
✓ Windows automation integration
✓ Scheduled task creation
✓ Error handling and logging
```

### 📊 Data Analysis & Reporting

```
✓ CloudWatch metrics statistical analysis
✓ Cost trend identification and forecasting
✓ Anomaly detection algorithms
✓ Data visualization (matplotlib, plotly)
✓ Threshold-based alerting
✓ Percentile calculations
✓ Time-series analysis
✓ Executive summary generation
✓ CSV/Excel data manipulation
✓ Interactive HTML dashboards
```

### 🔐 AWS Services & APIs

```
✓ Cost Explorer API (GetCostAndUsage, GetCostForecast)
✓ EC2 API (DescribeInstances, DescribeVolumes, DescribeSnapshots)
✓ CloudWatch API (GetMetricStatistics, PutMetricData)
✓ RDS API (DescribeDBInstances, DescribeDBSnapshots)
✓ ELB/ALB/NLB API (DescribeLoadBalancers, DescribeTargetHealth)
✓ S3 API (ListBuckets, GetBucketLifecycleConfiguration)
✓ Lambda API (ListFunctions, GetFunction)
✓ IAM API (GetAccountAuthorizationDetails)
✓ Organizations API (ListAccounts, DescribeOrganization)
✓ Multi-region API orchestration
✓ Pagination for large datasets
✓ Rate limiting and throttling management
✓ Error handling and retries
```

### 🏗️ Cloud Architecture & Optimization

```
✓ AWS pricing models (On-Demand, Reserved, Spot, Savings Plans)
✓ Resource lifecycle management
✓ Right-sizing methodologies
✓ Storage tier optimization (S3, EBS)
✓ Network cost optimization
✓ Reserved Instance vs Savings Plans analysis
✓ Compute Optimizer integration
✓ Well-Architected Framework (Cost Optimization Pillar)
```

### 🔧 DevOps & Automation

```
✓ Infrastructure as Code awareness
✓ CI/CD integration (GitHub Actions, GitLab CI)
✓ Automated testing (pytest, unittest)
✓ Version control (Git, semantic versioning)
✓ Documentation as code
✓ Configuration management
✓ Scheduled automation (cron, Windows Task Scheduler)
✓ Logging and monitoring
✓ Alerting and notifications
```

### 💼 Professional & Business Skills

```
✓ Cost-benefit analysis
✓ Technical documentation
✓ Stakeholder communication (exec summaries)
✓ Risk assessment (pre-cleanup validation)
✓ Project organization
✓ Problem-solving methodology
✓ ROI calculation and presentation
✓ Budget planning and forecasting
✓ Financial reporting
```

---

## 📜 License

This project is licensed under the **MIT License**.

### What is the MIT License?

The MIT License is one of the most permissive and widely-used open source licenses. It's short, simple, and allows you maximum freedom with the code.

### MIT License Summary

```
✓ Commercial use allowed
✓ Modification allowed
✓ Distribution allowed
✓ Private use allowed
✓ Must include original license and copyright notice
✗ No warranty provided
✗ No liability accepted
```

### What You Can Do

**✅ PERMITTED:**
- Use this tool in your company for AWS cost optimization
- Modify the code to fit your specific needs
- Distribute modified or unmodified versions
- Use in proprietary/commercial projects
- Include as part of larger projects
- Share with your team, clients, or community
- Create derivative works
- Use for any purpose (personal, commercial, educational)

**⚠️ CONDITIONS:**
- Include a copy of the MIT License with any distribution
- Include the original copyright notice
- Acknowledge that the software is provided "as is"

**❌ NOT ALLOWED:**
- Hold the authors liable for any damages
- Expect any warranty or guarantee
- Use authors' names for endorsement without permission

### Full License Text

```
MIT License

Copyright (c) 2025 Charles Bucher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Why MIT License for This Project?

**Chosen because:**
1. **Maximum freedom** - Users can do almost anything with the code
2. **Business-friendly** - Can be used in commercial environments without restrictions
3. **Simple & clear** - Easy to understand, no complex terms
4. **Wide adoption** - Compatible with most other licenses
5. **Community standard** - Encourages sharing and collaboration

**What this means for you:**
- Your company can use this tool to save money on AWS costs
- You can customize it for your specific environment
- You can package it with other tools
- You don't need to open-source your modifications (but contributions welcome!)
- No need to ask permission - just use it!

### Questions About the License?

**Can I use this at work?**  
✅ Yes! The MIT License explicitly allows commercial use.

**Do I need to share my modifications?**  
❌ No, but we'd love to see them! Consider contributing back.

**Can I sell a tool that includes this?**  
✅ Yes, as long as you include the MIT License notice.

**What if something breaks?**  
⚠️ No warranty provided. Use at your own risk. Test thoroughly before production use.

**Can I remove the license?**  
❌ No, you must include the MIT License text and copyright notice in any distribution.

### Related Documentation

- Full license text: [LICENSE](LICENSE) file in repository
- Open Source Initiative: [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)
- Choose a License: [https://choosealicense.com/licenses/mit/](https://choosealicense.com/licenses/mit/)

---

## ✅ Key Features

### 1. Comprehensive Resource Scanning

**Checks Across All Regions:**
- ✅ EC2 instances (running, stopped, idle)
- ✅ EBS volumes (unattached, underutilized)
- ✅ EBS snapshots (old, orphaned)
- ✅ RDS databases (idle, oversized)
- ✅ Elastic IPs (unattached)
- ✅ Load Balancers (ALB, NLB, CLB - no traffic)
- ✅ Lambda functions (unused)
- ✅ S3 buckets (lifecycle analysis)
- ✅ CloudWatch Logs (retention optimization)
- ✅ Unused Elastic Load Balancers

### 2. Intelligent Analysis

**Smart Detection:**
```
• CPU utilization analysis (7-day average)
• Network traffic monitoring
• Connection tracking (RDS)
• Last access timestamps
• Resource age calculation
• Usage pattern recognition
```

---

## 🚀 Quick Start

### Prerequisites

```bash
✓ AWS Account with read access
✓ AWS CLI configured (aws configure)
✓ Python 3.9+ installed
✓ PowerShell 7.0+ (for Windows scripts)
✓ IAM permissions for Cost Explorer and resource read access
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/charles-bucher/AWS-Cost-Optimization-Tool.git
cd AWS-Cost-Optimization-Tool

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Configure AWS credentials
aws configure

# 4. Run initial cost analysis
python cost_analyzer.py --full-scan

# 5. View the report
open reports/cost_optimization_report.html
```

### Quick Scan (5 minutes)

```bash
python cost_analyzer.py --quick-scan

# Expected Output:
✓ Scanning 3 regions...
✓ Found 5 idle EC2 instances → $450/month savings
✓ Found 12 unattached EBS volumes → $180/month savings
✓ Found 3 unattached Elastic IPs → $10.80/month savings

Total Potential Savings: $640.80/month ($7,689.60/year)
```

---

## 📞 Connect

**Charles Bucher** | Cloud Cost Optimization | FinOps Specialist

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/charles-bucher)

---

## 🌟 Related Projects

**AWS Portfolio Projects:**

- **[AWS Cloud Support Simulator](https://github.com/charles-bucher/AWS_Cloud_Support_Sim)** - Incident response scenarios
- **[AWS Error-Driven Troubleshooting Lab](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab)** - Hands-on troubleshooting
- **[AWS CloudOps Suite](https://github.com/charles-bucher/AWS_CloudOps_Suite)** - Infrastructure automation

---

## ⭐ Support This Project

**If this tool saved you money:**

1. ⭐ **Star this repository**
2. 📢 **Share your savings story**
3. 💼 **Use it at work**
4. 🤝 **Connect on LinkedIn**

---

<div align="center">

**Stop wasting cloud budget. Start optimizing today.**

Made with 💰 for FinOps engineers by cloud engineers

**[⬆ Back to Top](#aws-cost-optimization-tool)**

</div>

---

## 📋 Keywords for ATS/Search

AWS cost optimization, FinOps, cloud cost management, AWS Cost Explorer, cost analysis tool, cloud financial management, AWS resource optimization, cost reduction, cloud spend optimization, AWS billing, resource utilization analysis, right-sizing, Reserved Instances, Savings Plans, idle resource detection, cost allocation, cloud budget management, AWS cost reporting, infrastructure optimization, cloud waste reduction, boto3 automation, PowerShell AWS, cost governance, cloud efficiency, AWS pricing optimization, cloud economics, financial operations, AWS account management, cost-benefit analysis