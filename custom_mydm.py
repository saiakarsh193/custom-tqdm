import os
import time


def sec_to_formatted_time(seconds):
    seconds = int(seconds)
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    days = int(hours / 24)
    seconds -= minutes * 60
    minutes -= hours * 60
    hours -= days * 24
    if (days > 0):
        return f"{days}-{hours:02}:{minutes:02}:{seconds:02}"
    if (hours > 0):
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    return f"{minutes:02}:{seconds:02}"


class mydm:
    def __init__(self, vals):
        self.vals = list(vals)
        self.count = len(self.vals)
        self.thlen = os.get_terminal_size().columns # total horizontal length

        self.start_time = time.time()
        self.avg_time = 0
        self.last_call_time = time.time()

    def __iter__(self):
        for i in range(self.count + 1): 
            # we add 1 for making the percentage range from 0 -> 100
            # but when i is count + 1 (100%) it only prints and doesnt yield (no value to return)

            percentage = str(int(100 * i / self.count))
            percentage = (percentage + "%").rjust(4)
            
            # iter_prog = " " + str(i).rjust(len(str(self.count))) + "/" + str(self.count) + " "
            iter_prog = " " + str(i) + "/" + str(self.count) + " "

            cur_call_time = time.time()
            diff_call_time = cur_call_time - self.last_call_time
            self.last_call_time = cur_call_time
            self.avg_time = (self.avg_time * i + diff_call_time) / (i + 1)
            total_time = self.avg_time * self.count
            left_time = self.avg_time * (self.count - i)
            elapsed_time = cur_call_time - self.start_time

            time_prog = sec_to_formatted_time(elapsed_time) + "-" + sec_to_formatted_time(left_time)

            iters_per_sec = 1 / (1 if self.avg_time == 0 else self.avg_time)
            iters_per_sec = f"{iters_per_sec:.0f}ips"

            tim_ips_prog = "{" + time_prog + "|" + iters_per_sec + "}"

            bar_length = self.thlen - len(percentage) - len(iter_prog) - len(tim_ips_prog) - 2 # [===]
            bar_prog = " " + ("x" * int(bar_length * i / self.count)).ljust(bar_length, "-") + " "

            out_str = f"{percentage}{bar_prog}{iter_prog}{tim_ips_prog}"
            end_str = "" if i < self.count else "\n"
            print("\r" + out_str + end_str, end="")

            if i < self.count:
                yield self.vals[i]


if __name__ == "__main__":
    for i in mydm(range(100)):
        time.sleep(0.05)
