import numpy as np

class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of states
        emissions: list of observations
        B: Emmision probabilites
    """

    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between states and indexes
        """
        self.states_dict = dict(zip(self.states, list(range(self.N))))
        self.emissions_dict = dict(zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations. must be in the emmissions dict)
        Returns:
            nu: Porbability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        l = len(seq)
        var = np.zeros((l, self.N), dtype=int)
        vals = np.zeros((l, self.N))
        
        for x in range(self.N):
            var[0][x] = 0
            vals[0][x] = self.pi[x] * self.B[x, self.emissions_dict[seq[0]]]
            
        
        for i in range(1, l):
            for j in range(self.N):
                maxm = -1
                maxval = -1
                for k in range(self.N):
                    prod = vals[i - 1][k] * self.A[k][j] * self.B[j][self.emissions_dict[seq[i]]]

                    if prod > maxval:
                        maxm = k
                        maxval = prod

                var[i][j] = maxm    
                vals[i][j] = maxval
                
        
        maxm = -1
        maxval = -1
        
        for j in range(self.N):
            prod = vals[l - 1][j]
            if prod > maxval:
                maxm = j
                maxval = prod
                
        
        states = [maxm]
        for i in range(l - 1, 0, -1):

            states.append(var[i][states[-1]])

        states.reverse()

        self.states_dict = {value: key for key, value in self.states_dict.items()}
        hiddenStatesSequence = [self.states_dict[state] for state in states]
        return hiddenStatesSequence

