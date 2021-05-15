from contextlib import ContextDecorator
from datetime import datetime, timezone


class OperationTelemetry(object):
    start_timestamp = None
    end_timestamp = None
    result_status = None

    def start_keeping_time(self, starting_time: datetime = None) -> None:
        if starting_time is not None:
            self.start_timestamp = starting_time
        else:
            self.start_timestamp = datetime.now(timezone.utc)

    def stop_keeping_time(self, stop_time: datetime = None) -> None:
        if stop_time is not None:
            self.end_timestamp = stop_time
        else:
            self.end_timestamp = datetime.now(timezone.utc)


class OperationTelemetryContext(OperationTelemetry):
    def __enter__(self, start=None):
        super().start_keeping_time(start)
        return self

    def __exit__(self, stop=None):
        super().stop_keeping_time(stop)
        return self


class OperationTelemetryDecorator(ContextDecorator, OperationTelemetryContext):
    pass
