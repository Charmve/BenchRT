load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")
load("@third_party//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

filegroup(
    name = "utils-srcs",
    srcs = glob(
        ["*.py"],
        exclude = [
            "*_test.py",
            "json_profile_merger.py",
            "bigquery_upload.py",
            "storage_upload.py",
        ],
    ),
)

py_library(
    name = "utils",
    srcs = [":utils-srcs"],
    deps = [
        requirement("absl-py"),
        requirement("certifi"),
        requirement("chardet"),
        requirement("funcsigs"),
        requirement("idna"),
        requirement("numpy"),
        requirement("pbr"),
        requirement("psutil"),
        requirement("pyasn1"),
        requirement("pyasn1-modules"),
        requirement("rsa"),
        requirement("scipy"),
        requirement("six"),
        requirement("urllib3"),
        requirement("PyYAML"),
    ],
)

py_library(
    name = "google-common",
    deps = [
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
    name = "bigquery_upload",
    srcs = ["bigquery_upload.py"],
    deps = [
        # This is a workaround for https://github.com/bazelbuild/rules_python/issues/14,
        # google-cloud-bigquery must be listed first.
        requirement("google-cloud-bigquery"),
        requirement("absl-py"),
        requirement("futures"),
        ":google-common",
    ],
)

py_binary(
    name = "storage_upload",
    srcs = ["storage_upload.py"],
    deps = [
        # This is a workaround for https://github.com/bazelbuild/rules_python/issues/14,
        # google-cloud-storage must be listed first.
        requirement("google-cloud-storage"),
        requirement("absl-py"),
        ":google-common",
    ],
)

py_binary(
    name = "qbuild_dbg",
    srcs = ["qbuild_dbg.py"],
    deps = [
        # This is a workaround for https://github.com/bazelbuild/rules_python/issues/14,
        # google-cloud-storage must be listed first.
        requirement("google-cloud-storage"),
        requirement("absl-py"),
        ":google-common",
    ],
)

py_binary(
    name = "qsutil_test",
    srcs = ["qsutil_test.py"],
    deps = [
        ":utils",
        # This is a workaround for https://github.com/bazelbuild/rules_python/issues/14,
        # google-cloud-storage must be listed first.
        requirement("absl-py"),
        ":google-common",
    ],
)

py_binary(
    name = "json_profiles_merger",
    srcs = ["json_profiles_merger.py"],
    deps = [
        ":utils",
        requirement("absl-py"),
    ],
)

py_test(
    name = "bazel_test",
    size = "small",
    srcs = ["bazel_test.py"],
    deps = [
        ":utils",
        requirement("mock"),
    ],
)

py_test(
    name = "values_test",
    size = "small",
    srcs = ["values_test.py"],
    deps = [
        ":utils",
        requirement("mock"),
    ],
)

py_test(
    name = "json_profiles_merger_lib_test",
    size = "small",
    srcs = ["json_profiles_merger_lib_test.py"],
    deps = [
        ":utils",
        requirement("mock"),
    ],
)

py_test(
    name = "benchmark_config_test",
    size = "small",
    srcs = ["benchmark_config_test.py"],
    deps = [
        ":utils",
    ],
)
