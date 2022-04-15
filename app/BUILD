load("@rules_python//python:defs.bzl", "py_library", "py_test")
load("@my_python_deps//:requirements.bzl", "requirement")

py_binary(
    name = "run",
    srcs = ["run.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    visibility = ["//visibility:public"],
    deps = [
        ":app",
        requirement("uvicorn"),
    ],
)

py_library(
    name = "app",
    srcs = ["main.py"],
    srcs_version = "PY3",
    deps = [requirement("fastapi")],
)

py_test(
    name = "test",
    srcs = [
        "test.py",
    ],
    # main = "test.py",
    args = [
        "--capture=no",
    ],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":app",
        requirement("requests"),
        requirement("fastapi"),
        requirement("pytest"),
    ],
)

