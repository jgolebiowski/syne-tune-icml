# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
from benchmarking.nursery.benchmark_automl.benchmark_main import main


if __name__ == "__main__":
    from benchmarking.nursery.benchmark_dehb.baselines import methods
    from benchmarking.nursery.benchmark_dehb.benchmark_definitions import (
        benchmark_definitions,
    )

    extra_args = [
        dict(
            name="--num_brackets",
            type=int,
            required=False,
            help="number of brackets",
        ),
        # TODO: Move to benchmark_hypertune once this is in!
        # dict(
        #     "--num_samples",
        #     type=int,
        #     default=50,
        #     help="Number of samples for Hyper-Tune distribution",
        # ),
    ]

    def map_extra_args(args) -> dict:
        return dict(
            num_brackets=args.num_brackets,
        )

    main(methods, benchmark_definitions, extra_args, map_extra_args)