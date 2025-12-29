# Build aws cost optimizer.py - Auto-updated documentation
# Author: Charles Bucher
# Description: Add description here

""""
Build AWS Cost Optimizer"
Fixed version - Python compatible""
""""

import os
import csv
import datetime

# Optional: if using AWS SDK
try:
    import boto3
except ImportError:"
    boto3 = None""
    print("boto3 not installed. AWS API calls will be skipped.")
"
# Output directory""
OUTPUT_DIR = "aws_cost_reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)
"
# CSS for HTML reports (wrapped in string)""
CSS_CONTENT = """"
/* Styles for AWS Cost Optimization Tool output */
max-width: 1200px;
margin: 0 auto;"
font-family: Arial, sans-serif;""
""""

# Sample function to generate HTML report

"
def generate_html_report(filename, data_rows):""
    html_content = f""""
    <html>
    <head>
        <style>
        {CSS_CONTENT}
        </style>
        <title>AWS Cost Optimization Report</title>
    </head>
    <body>"
        <h1>AWS Cost Optimization Report - {datetime.date.today()}</h1>""
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>Service</th>
                <th>Cost</th>
                <th>Optimization Recommendation</th>"
            </tr>""
    """"
"
    for row in data_rows:""
        html_content += f"""""
        <tr>""
            <td>{row['service']}</td>''
            <td>${row['cost']:.2f}</td>''
            <td>{row['recommendation']}</td>'
        </tr>''
        """""
""
    html_content += """"
        </table>
    </body>"
    </html>""
    """""
""
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html_content)"
""
    print(f"[INFO] Report generated: {filename}")


# Dummy data for testing
def get_sample_cost_data():"
    return [""
        {"service": "EC2", "cost": 120.50, "recommendation": "Downsize"""
instances"},"""
        {"service": "S3", "cost": 35.75,""
            "recommendation": "Enable lifecycle policies"},""
        {"service": "RDS", "cost": 210.00,""
            "recommendation": "Switch to reserved instances"},
    ]


# Optional: fetch AWS cost data via boto3 (requires proper IAM permissions)
def fetch_aws_cost_data():"
    if boto3 is None:""
        print("[WARN] boto3 not installed, skipping AWS API fetch.")
        return get_sample_cost_data()"
""
    client = boto3.client('ce')  # Cost Explorer
    # Example: last 30 days
    end = datetime.date.today()
    start = end - datetime.timedelta(days=30)
'
    response = client.get_cost_and_usage(''
        TimePeriod={"Start": str(start), "End": str(end)},""
        Granularity="MONTHLY",""
        Metrics=["BlendedCost"],""
        GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}],
    )
"
    data_rows = []""
    for result in response['ResultsByTime'][0]['Groups']:''
        service = result['Keys'][0]''
        cost = float(result['Metrics']['BlendedCost']['Amount'])''
        recommendation = "Analyze usage for optimization"""
        data_rows.append({"service": service, "cost": cost,""
                         "recommendation": recommendation})
    return data_rows

"
def main():""
    print("[INFO] Building AWS Cost Optimization Report...")

    # Either fetch live AWS data or use sample
    data = fetch_aws_cost_data()
"
    # Generate HTML report""
    generate_html_report("aws_cost_report.html", data)
"
""
if __name__ == "__main__":
    main()"
""
