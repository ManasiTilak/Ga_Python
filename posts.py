import os
from dotenv import load_dotenv
#Google Analytics API Imports
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
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
        # offset=100000,
    )
    response = client.run_report(request)
    write_json(response)

def print_run_report_response(response):
    """Prints results of a runReport call."""
    print(f"{response.row_count} rows received")
    for dimensionHeader in response.dimension_headers:
        print(f"Dimension header name: {dimensionHeader.name}")
    for metricHeader in response.metric_headers:
        metric_type = MetricType(metricHeader.type_).name
        print(f"Metric header name: {metricHeader.name})")

    print("Report result:")
    for rowIdx, row in enumerate(response.rows):
        print(f"\nRow {rowIdx}")
        for i, dimension_value in enumerate(row.dimension_values):
            dimension_name = response.dimension_headers[i].name
            print(f"{dimension_name}: {dimension_value.value}")

        for i, metric_value in enumerate(row.metric_values):
            metric_name = response.metric_headers[i].name
            print(f"{metric_name}: {metric_value.value}")

def write_json(response):
    with open('data/posts.json', "w")as f:
        for rowIdx, row in enumerate(response.rows):
            f.write(f"\nRow {rowIdx}")
            for i, dimension_value in enumerate(row.dimension_values):
                dimension_name = response.dimension_headers[i].name
                f.write(f"{dimension_name}: {dimension_value.value}")

            for i, metric_value in enumerate(row.metric_values):
                metric_name = response.metric_headers[i].name
                f.write(f"{metric_name}: {metric_value.value}")

if __name__ == "__main__":
    run_report()
    