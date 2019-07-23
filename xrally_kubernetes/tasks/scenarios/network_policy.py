from rally.task import scenario

from xrally_kubernetes.tasks import scenario as common_scenario
import pdb
@scenario.configure(name="Kubernetes.create_network_policy",
                    platform="kubernetes")
class CreateAndDeleteNetworkPolicy(common_scenario.BaseKubernetesScenario):

    def run(self):
        """Create network policy, wait until it won't be active and then delete it.

        :param status_wait: wait namespace status after creation
        """
        self.client.create_network_policy()