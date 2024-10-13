import asyncio
import time
from bot.utils import logger
from datetime import datetime, timedelta


class Watchdog:
    """
    Class to track the number of errors over a specified time window and introduce a sleep (pause)
    if the number of errors exceeds a threshold within the given time period.
    """

    def __init__(self, client_name, max_errors=5, time_window=timedelta(minutes=1), sleep_duration=timedelta(hours=1),
                 each_error_sleep_time=timedelta(minutes=0.5)):
        """
        Initialize the watchdog with:
        :param max_errors: The maximum number of errors before sleeping.
        :param time_window: The time window within which to track errors.
        :param sleep_duration: The duration of the sleep (in seconds) after reaching the error limit.
        """
        self.client_name = client_name
        self.max_errors = max_errors
        self.time_window = time_window
        self.sleep_duration = sleep_duration
        self.error_timestamps = []  # List to store error timestamps
        self.each_error_sleep_time = each_error_sleep_time

    async def track_error(self):
        """
        Track a new error. If the number of errors within the time window exceeds the threshold,
        the system will sleep for the specified duration and reset the error log.
        """
        current_time = datetime.now()

        # Remove old errors that are outside the time window
        self.error_timestamps = [timestamp for timestamp in self.error_timestamps
                                 if current_time - timestamp < self.time_window]

        # Add the current error's timestamp
        self.error_timestamps.append(current_time)

        # If the number of errors exceeds the threshold, trigger sleep
        if len(self.error_timestamps) >= self.max_errors:
            logger.warning(f"{self.client_name} | Max errors reached. Sleeping for "
                           f"<y>{self.sleep_duration.total_seconds()/60}</y> min.")
            await asyncio.sleep(self.sleep_duration.total_seconds())  # Use asyncio.sleep for non-blocking sleep
            self.error_timestamps.clear()  # Reset the error log after sleeping
        else:
            logger.warning(f"{self.client_name} | An error has been detected. Sleeping for"
                           f" <y>{self.each_error_sleep_time.total_seconds()/60}</y> min.")
            await asyncio.sleep(self.each_error_sleep_time.total_seconds())


