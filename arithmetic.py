class arithmetic:
    """
    """

    def __init__(self, first_term, last_term, common_difference):
        """ first_term is the first value of the sequence,
            last_term is the total numbers in the sequence
            common_difference is the value between the values is the sequence
        """
        self.first_term = first_term
        self.last_term = last_term
        self.common_difference = common_difference

    def n_term(self):
        n_first = int(self.first_term)
        the_difference = int(self.common_difference)

        value = n_first + (int(self.last_term) - 1) * the_difference
        return value

    def term_calculator(self, term):
        n_first = int(self.first_term)
        the_difference = int(self.common_difference)

        value = n_first + (int(term) - 1) * the_difference
        return value

    def sequence(self):
        if int(self.last_term) > 10:
            """ First 4 values if larger than 10 digits in sequence
            """
            counter = 1
            first_four = list()
            while counter < 5:
                first_four.append(self.term_calculator(counter))
                counter += 1
            first_four.append("...")

            second_counter = int(self.last_term) - 3
            while second_counter < (int(self.last_term) + 1):
                first_four.append(self.term_calculator(second_counter))
                second_counter += 1
            return first_four
        else:
            sequence_holder = list()
            third_counter = 1
            while third_counter < (int(self.last_term) + 1):
                sequence_holder.append(self.term_calculator(third_counter))
                third_counter += 1
            return sequence_holder

    def sum(self):
        last_value = self.n_term()
        sum_result = self.last_term * ((self.first_term + last_value) / 2)
        return sum_result
