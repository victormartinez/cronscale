from kubernetes import config

config.load_incluster_config()

from kubernetes import client
from kubernetes.client.models.v2beta1_horizontal_pod_autoscaler import (
    V2beta1HorizontalPodAutoscaler,
)

import settings


def scale(
    project_name: str, min_replicas: int, max_replicas: int
) -> V2beta1HorizontalPodAutoscaler:
    config = settings.PROJECTS[project_name]["HPA"]

    api_client = client.AutoscalingV2beta1Api(client.ApiClient())
    v2beta1_hpa = api_client.read_namespaced_horizontal_pod_autoscaler(
        config["NAME"], config["NAMESPACE"]
    )
    v2beta1_hpa.spec.min_replicas = min_replicas
    v2beta1_hpa.spec.max_replicas = max_replicas
    v2beta1_hpa.status = None

    return api_client.patch_namespaced_horizontal_pod_autoscaler(
        config["NAME"], config["NAMESPACE"], v2beta1_hpa
    )
