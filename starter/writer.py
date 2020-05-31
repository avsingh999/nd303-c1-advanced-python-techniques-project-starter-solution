from enum import Enum
import csv


class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported
    output formatting options.
    """

    def __init__(self):
        pass

    def write(self, format, data, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat
        selected calls the appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting
         output e.g. filename
        :return: bool representing if write successful or not
        """
        if format == OutputFormat.display.value:
            print("OK")
            value = list(data[0].__dict__.keys())
            print(*value, sep=('     :    '))
            for d in data:
                print(*d.__dict__.values(), sep=(':    '))
            return True

        if format == OutputFormat.csv_file.value:
            print("Writing to csv file ....")
            keys = list(data[0].__dict__.keys())

            with open('output.csv', 'w') as f:
                keys.append('miss_distance_kilometers')
                keys.append('date')
                writer = csv.DictWriter(f, fieldnames=keys)

                writer.writeheader()
                for d in data:
                    d_dict = d.__dict__
                    for o in d.orbits:
                        d_dict['miss_distance_kilometers'] =
                        o.miss_distance_kilometers
                        d_dict['date'] = o.close_approach_date
                        writer.writerow(d_dict)
            return True
