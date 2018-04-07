from tabula import convert_into
# ALL
convert_into("test.pdf", "test_all.csv", output_format="csv", options="--pages all")
# Page
convert_into("test.pdf", "test_10-20.csv", output_format="csv", options="--pages 10-20")
