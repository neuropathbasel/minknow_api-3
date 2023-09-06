# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from minknow_api import instance_pb2 as minknow__api_dot_instance__pb2


class InstanceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_version_info = channel.unary_unary(
                '/minknow_api.instance.InstanceService/get_version_info',
                request_serializer=minknow__api_dot_instance__pb2.GetVersionInfoRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.GetVersionInfoResponse.FromString,
                )
        self.get_output_directories = channel.unary_unary(
                '/minknow_api.instance.InstanceService/get_output_directories',
                request_serializer=minknow__api_dot_instance__pb2.GetOutputDirectoriesRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.OutputDirectories.FromString,
                )
        self.get_default_output_directories = channel.unary_unary(
                '/minknow_api.instance.InstanceService/get_default_output_directories',
                request_serializer=minknow__api_dot_instance__pb2.GetDefaultOutputDirectoriesRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.OutputDirectories.FromString,
                )
        self.set_output_directory = channel.unary_unary(
                '/minknow_api.instance.InstanceService/set_output_directory',
                request_serializer=minknow__api_dot_instance__pb2.SetOutputDirectoryRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.SetOutputDirectoryResponse.FromString,
                )
        self.set_reads_directory = channel.unary_unary(
                '/minknow_api.instance.InstanceService/set_reads_directory',
                request_serializer=minknow__api_dot_instance__pb2.SetReadsDirectoryRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.SetReadsDirectoryResponse.FromString,
                )
        self.get_disk_space_info = channel.unary_unary(
                '/minknow_api.instance.InstanceService/get_disk_space_info',
                request_serializer=minknow__api_dot_instance__pb2.GetDiskSpaceInfoRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.GetDiskSpaceInfoResponse.FromString,
                )
        self.stream_disk_space_info = channel.unary_stream(
                '/minknow_api.instance.InstanceService/stream_disk_space_info',
                request_serializer=minknow__api_dot_instance__pb2.StreamDiskSpaceInfoRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.GetDiskSpaceInfoResponse.FromString,
                )
        self.get_machine_id = channel.unary_unary(
                '/minknow_api.instance.InstanceService/get_machine_id',
                request_serializer=minknow__api_dot_instance__pb2.GetMachineIdRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.GetMachineIdResponse.FromString,
                )
        self.stream_instance_activity = channel.unary_stream(
                '/minknow_api.instance.InstanceService/stream_instance_activity',
                request_serializer=minknow__api_dot_instance__pb2.StreamInstanceActivityRequest.SerializeToString,
                response_deserializer=minknow__api_dot_instance__pb2.StreamInstanceActivityResponse.FromString,
                )


class InstanceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_version_info(self, request, context):
        """Current version information includes:
        - Minknow version
        - Protocols version
        - Distribution version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_output_directories(self, request, context):
        """Returns various directory locations where minknow is outputting data. The paths are absolute paths, 
        local to the machine where minknow is installed

        the `output` base directory can be changed internally
        the `logs` directory will not be changed and can be stored
        the `reads` directory is determined  by the read writer config
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_default_output_directories(self, request, context):
        """See `get_output_directories`, but this will always return the paths that are defined in the config when the instance
        of minknow has started

        Since 1.11
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_output_directory(self, request, context):
        """Set the base directory to where all data will be output. Must be an absolute directory

        Fails with INVALID_ARGUMENT if `value` is not absolute.
        Fails with FAILED_PRECONDITION if this is called during acquisition

        Since 1.11
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_reads_directory(self, request, context):
        """Set the reads directory where read files (hdf5, fastq, protobuf) will be output

        Fails with INVALID_ARGUMENT if `value` is not absolute.
        Fails with FAILED_PRECONDITION if this is called during acquisition

        Since 1.12
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_disk_space_info(self, request, context):
        """Returns information about the amount of disk space available, how much
        space is needed to stop an experiment cleanly and if MinKNOW thinks
        that the free disk-space is approaching or past this limit

        Since 1.11
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stream_disk_space_info(self, request, context):
        """Stream information about the amount of disk space available, how quickly
        it is being used, how much space is needed to stop an experiment cleanly
        and if MinKNOW thinks that the free disk-space is approaching or past
        this limit

        Since 4.0
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_machine_id(self, request, context):
        """Find the machine id MinKNOW uses for this machine.

        This is expected to be a descriptive string for the machine, MinKNOW currently uses the network hostname.

        note: This is the identifier used when sending telemetry data for this instance.

        Since 1.11
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stream_instance_activity(self, request, context):
        """Find a summary of activity on the instance.

        The information available from this request is also available from other rpc's - this call is intended
        as a performance improvement for users who watch a large number of streams (specifically over
        web socket transport).

        Use this request to find information about the current device, flow cell, protocol and acquisition state.

        Since 3.2
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InstanceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_version_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_version_info,
                    request_deserializer=minknow__api_dot_instance__pb2.GetVersionInfoRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.GetVersionInfoResponse.SerializeToString,
            ),
            'get_output_directories': grpc.unary_unary_rpc_method_handler(
                    servicer.get_output_directories,
                    request_deserializer=minknow__api_dot_instance__pb2.GetOutputDirectoriesRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.OutputDirectories.SerializeToString,
            ),
            'get_default_output_directories': grpc.unary_unary_rpc_method_handler(
                    servicer.get_default_output_directories,
                    request_deserializer=minknow__api_dot_instance__pb2.GetDefaultOutputDirectoriesRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.OutputDirectories.SerializeToString,
            ),
            'set_output_directory': grpc.unary_unary_rpc_method_handler(
                    servicer.set_output_directory,
                    request_deserializer=minknow__api_dot_instance__pb2.SetOutputDirectoryRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.SetOutputDirectoryResponse.SerializeToString,
            ),
            'set_reads_directory': grpc.unary_unary_rpc_method_handler(
                    servicer.set_reads_directory,
                    request_deserializer=minknow__api_dot_instance__pb2.SetReadsDirectoryRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.SetReadsDirectoryResponse.SerializeToString,
            ),
            'get_disk_space_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_disk_space_info,
                    request_deserializer=minknow__api_dot_instance__pb2.GetDiskSpaceInfoRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.GetDiskSpaceInfoResponse.SerializeToString,
            ),
            'stream_disk_space_info': grpc.unary_stream_rpc_method_handler(
                    servicer.stream_disk_space_info,
                    request_deserializer=minknow__api_dot_instance__pb2.StreamDiskSpaceInfoRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.GetDiskSpaceInfoResponse.SerializeToString,
            ),
            'get_machine_id': grpc.unary_unary_rpc_method_handler(
                    servicer.get_machine_id,
                    request_deserializer=minknow__api_dot_instance__pb2.GetMachineIdRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.GetMachineIdResponse.SerializeToString,
            ),
            'stream_instance_activity': grpc.unary_stream_rpc_method_handler(
                    servicer.stream_instance_activity,
                    request_deserializer=minknow__api_dot_instance__pb2.StreamInstanceActivityRequest.FromString,
                    response_serializer=minknow__api_dot_instance__pb2.StreamInstanceActivityResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'minknow_api.instance.InstanceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InstanceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_version_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/minknow_api.instance.InstanceService/get_version_info',
            minknow__api_dot_instance__pb2.GetVersionInfoRequest.SerializeToString,
            minknow__api_dot_instance__pb2.GetVersionInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_output_directories(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/minknow_api.instance.InstanceService/get_output_directories',
            minknow__api_dot_instance__pb2.GetOutputDirectoriesRequest.SerializeToString,
            minknow__api_dot_instance__pb2.OutputDirectories.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_default_output_directories(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/minknow_api.instance.InstanceService/get_default_output_directories',
            minknow__api_dot_instance__pb2.GetDefaultOutputDirectoriesRequest.SerializeToString,
            minknow__api_dot_instance__pb2.OutputDirectories.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def set_output_directory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/minknow_api.instance.InstanceService/set_output_directory',
            minknow__api_dot_instance__pb2.SetOutputDirectoryRequest.SerializeToString,
            minknow__api_dot_instance__pb2.SetOutputDirectoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def set_reads_directory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/minknow_api.instance.InstanceService/set_reads_directory',
            minknow__api_dot_instance__pb2.SetReadsDirectoryRequest.SerializeToString,
            minknow__api_dot_instance__pb2.SetReadsDirectoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_disk_space_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/minknow_api.instance.InstanceService/get_disk_space_info',
            minknow__api_dot_instance__pb2.GetDiskSpaceInfoRequest.SerializeToString,
            minknow__api_dot_instance__pb2.GetDiskSpaceInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stream_disk_space_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/minknow_api.instance.InstanceService/stream_disk_space_info',
            minknow__api_dot_instance__pb2.StreamDiskSpaceInfoRequest.SerializeToString,
            minknow__api_dot_instance__pb2.GetDiskSpaceInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_machine_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/minknow_api.instance.InstanceService/get_machine_id',
            minknow__api_dot_instance__pb2.GetMachineIdRequest.SerializeToString,
            minknow__api_dot_instance__pb2.GetMachineIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stream_instance_activity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/minknow_api.instance.InstanceService/stream_instance_activity',
            minknow__api_dot_instance__pb2.StreamInstanceActivityRequest.SerializeToString,
            minknow__api_dot_instance__pb2.StreamInstanceActivityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
