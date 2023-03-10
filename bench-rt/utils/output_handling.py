# Copyright 2019 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import csv
import getpass
import os
import socket

import utils.logger as logger


def export_csv(data_directory, filename, data):
    """Exports the content of data to a csv file in data_directory

    Args:
      data_directory: the directory to store the csv file.
      filename: the name of the .csv file.
      data: the collected data to be exported.

    Returns:
      The path to the newly created csv file.
    """
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    csv_file_path = os.path.join(data_directory, filename)
    logger.log("Writing raw data into csv file: %s" % str(csv_file_path))

    with open(csv_file_path, "w") as csv_file:
        hostname = socket.gethostname()
        username = getpass.getuser()
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            [
                "project_source",
                "project_commit",
                "bazel_commit",
                "run",
                "wall",
                "cpu",
                "cpu_user",
                "cpu_system",
                "memory",
                "command",
                "expressions",
                "hostname",
                "username",
                "options",
                "exit_status",
                "started_at",
                "platform",
                "project_label",
            ]
        )

        for (bazel_commit, project_commit), data_item in data.items():
            command, expressions, options = data_item["args"]
            non_measurables = data_item["non_measurables"]
            for idx, run in enumerate(data_item["results"], start=1):
                csv_writer.writerow(
                    [
                        non_measurables["project_source"],
                        project_commit,
                        bazel_commit,
                        idx,
                        run["wall"],
                        run["cpu"],
                        run["cpu_user"],
                        run["cpu_system"],
                        run["memory"],
                        command,
                        expressions,
                        hostname,
                        username,
                        options,
                        run["exit_status"],
                        run["started_at"],
                        non_measurables["platform"],
                        non_measurables["project_label"],
                    ]
                )
    return csv_file_path


def export_file(data_directory, filename, content):
    """Exports the content of data to a file in data_directory

    Args:
      data_directory: the directory to store the file.
      filename: the name of the file.
      content: the content to be exported.

    Returns:
      The path to the newly created file.
    """
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    out_file_path = os.path.join(data_directory, filename)

    with open(out_file_path, "w") as out_file:
        out_file.write(content)

    return out_file_path
