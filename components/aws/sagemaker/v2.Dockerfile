# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 

# Dockerfile for v2, to use the v2.Dockerfile.dockerignore, before building:
# export DOCKER_BUILDKIT=1 

FROM amazonlinux:2

ENV PYTHONPATH /app

RUN yum update -y \
 && yum install -y -q \
    ca-certificates \
    python3 \
    wget \
    unzip

COPY requirements_v2.txt .
RUN pip3 install -r requirements_v2.txt

WORKDIR /app

COPY . .

ENTRYPOINT [ "bash" ]