"""!!!DO NOT USE!!!

Distribution related class for Tensorflow backend.

This is just a prototype and we might want to unify it
with other backends in the future.
"""
import tensorflow as tf
from tensorflow.experimental import dtensor


def list_devices(device_type=None):
    """Return all the available devices based on the device type.

    Note that this should return the global devices in a distributed setting.

    Args:
        device_type: string of `"cpu"`, `"gpu"` or `"tpu"`. Default to `gpu` or
        `tpu` if available when device_type is not provided. Otherwise will
        return the `cpu` devices.

    Return:
        List of devices that are available for distribute computation.
    """
    device_type = (
        device_type.upper() if device_type else dtensor.preferred_device_type()
    )

    # DTensor doesn't support getting global devices, even when knowing the
    # Mesh. Use TF API instead to get global devices. Coordinator service is
    # enabled by default with DTensor, so that list_logical_devices() returns
    # a list of global devices. More context can be found in b/254911601.
    return tf.config.list_logical_devices(device_type=device_type)


def to_dtensor_mesh(device_mesh):
    """Convert the DeviceMesh to Tensorflow backend specific Mesh.

    Args:
        device_mesh: DeviceMesh instance to convert.

    Returns:
        A `tf.dtensor.Mesh` instance.
    """
    mesh_dims = list(zip(device_mesh.axis_names, device_mesh.shape))
    return dtensor.create_distributed_mesh(
        mesh_dims=mesh_dims, local_devices=device_mesh.devices.flatten()
    )


def to_dtensor_layout(tensor_layout):
    """Convert the TensorLayout to Tensorflow backend specific Sharding.

    Args:
        tensor_layout: TensorLayout instance to convert.

    Returns:
        A `tf.dtensor.Layout` instance.
    """
    if tensor_layout.device_mesh is None:
        raise ValueError(
            "Cannot create sharding when device mesh is not set for "
            "TensorLayout."
        )

    sharding_specs = [
        axis if axis else dtensor.UNSHARDED for axis in tensor_layout.axes
    ]
    dtensor_mesh = to_dtensor_mesh(tensor_layout.device_mesh)
    return dtensor.Layout(sharding_specs=sharding_specs, mesh=dtensor_mesh)