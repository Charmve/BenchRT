load("@rules_python//python:defs.bzl", "py_binary")
load("@third_party//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_binary(
    name = "generate_report",
    srcs = ["generate_report.py"],
    deps = [
        "//utils",
        # This is a workaround for https://github.com/bazelbuild/rules_python/issues/14,
        # google-cloud-bigquery must be listed first.
        requirement("google-cloud-bigquery"),
        requirement("cachetools"),
        requirement("google-api-core"),
        requirement("google-auth"),
        requirement("google-cloud-core"),
        requirement("google-resumable-media"),
        requirement("googleapis-common-protos"),
        requirement("protobuf"),
        requirement("pytz"),
        requirement("requests"),
    ],
)

py_binary(
    name = "generate_master_report",
    srcs = ["generate_master_report.py"],
    deps = [
        "//utils",
        # This is a workaround for https://github.com/bazelbuild/rules_python/issues/14,
        # google-cloud-bigquery must be listed first.
        requirement("google-cloud-bigquery"),
        requirement("cachetools"),
        requirement("google-api-core"),
        requirement("google-auth"),
        requirement("google-cloud-core"),
        requirement("google-resumable-media"),
        requirement("googleapis-common-protos"),
        requirement("protobuf"),
        requirement("pytz"),
        requirement("requests"),
    ],
)
