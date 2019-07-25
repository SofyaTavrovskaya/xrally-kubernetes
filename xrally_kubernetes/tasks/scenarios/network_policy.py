from rally.task import scenario

from xrally_kubernetes.tasks import scenario as common_scenario

@scenario.configure(name="Kubernetes.create_and_delete_network_policy",
                    platform="kubernetes")
class CreateAndDeleteNetworkPolicy(common_scenario.BaseKubernetesScenario):

    def run(self, status_wait=True):
        """Create network policy, wait until it won't be active and then delete it.

        :param status_wait: wait namespace status after creation
        """

        name = self.client.create_network_policy(
            namespace="default",
            status_wait=status_wait,
        )
        self.client.delete_network_policy(
            name=name,
            namespace="default"
        )