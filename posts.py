import os
from dotenv import load_dotenv
#Google Analytics API Imports
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

#Setting up environment variables
load_dotenv()
PROPERTY = os.getenv('PROPERTY')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account.json'

def run_report(property_id=PROPERTY):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{PROPERTY}",
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="90daysAgo", end_date="today")],
        limit=5,
    )
    response = client.run_report(request)
    # print(response)
    write_json(response)

def write_json(response):
    with open('data/posts.json', "w")as f:
        for rowIdx, row in enumerate(response.rows):
            f.write("\n")
            for i, dimension_value in enumerate(row.dimension_values):
                f.write(f"{dimension_value.value}|")

            for i, metric_value in enumerate(row.metric_values):
                f.write("\t\t")
                metric_name = response.metric_headers[i].name
                f.write(f"{metric_name}: {metric_value.value}")

if __name__ == "__main__":
    run_report()
    