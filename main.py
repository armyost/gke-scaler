from google.cloud import container_v1
# from google.cloud import compute_v1
from jproperties import Properties

configs = Properties()
        
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

val_scale_out = int(configs.get("SCALE_OUT").data)
val_scale_in = int(configs.get("SCALE_IN").data)

print("### START - Call properties ")
print("###### SCALE_OUT VALUE : %d" % val_scale_out)  
print("###### SCALE_IN VALUE : %d" % val_scale_in)
print("### END - Call properties ")

def scale_out_function(argument):
    # Create a client
    client = container_v1.ClusterManagerClient()

    # Initialize request argument(s)
    request_val = container_v1.SetNodePoolSizeRequest(
        name="projects/sample-prj-440709/locations/us-central1-c/clusters/my-first-cluster-1/nodePools/default-pool",
        node_count=val_scale_out
    )
    
    # Make the request
    response = client.set_node_pool_size(request=request_val)

    # Handle the response
    print("### START - Send request ")
    print(response)
    print("### END - Send request ")

    return 200

def scale_in_function(argument):
    # Create a client
    client = container_v1.ClusterManagerClient()

    # Initialize request argument(s)
    request_val = container_v1.SetNodePoolSizeRequest(
        name="projects/sample-prj-440709/locations/us-central1-c/clusters/my-first-cluster-1/nodePools/default-pool",
        node_count=val_scale_in
    )
    
    # Make the request
    response = client.set_node_pool_size(request=request_val)

    # Handle the response
    print("### START - Send request ")
    print(response)
    print("### END - Send request ")

    return 200