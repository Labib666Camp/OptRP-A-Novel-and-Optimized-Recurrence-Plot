from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

class OptimumRecurrencePlot:
  def __init__(self,sig,dimension):
    self.dimension = dimension
    self.sig = sig
    
  def embed(self,tau=1):
    m = len(self.sig) - (self.dimension)*tau
    return np.array([self.sig[i:i + (self.dimension - 1)*tau + 1: tau] for i in range(m)])

  def RPHistogram(self,RP):
    r_idxs = np.where(RP!=10)
    RP = RP[r_idxs].flatten()
    rands,freqs = np.unique(RP,return_counts=True)
    N = RP.shape[0]
    probs = freqs/N
    return probs
  
  def CalculateEntropy(self,probs):
    en = -np.sum(probs*np.log(probs))
    sh = probs.shape[0]
    l = round(math.log(sh),2)
    entropy = round(en/l,3)
    return entropy
  
  def OptimumRP(self,em,eps):
    D = euclidean_distances(em,em)
    cinds = np.where(D>eps)
    c = 1 / np.amax(D[cinds])
    x_0 = np.amin(D[cinds])
    a = -0.99/np.log(c*x_0)
    rp = np.where(D<=eps,1.0,-a*np.log(c*D))
    return rp

  def GetOptimumRP(self):
    embedding = self.embed(self.sig)
    D = euclidean_distances(embedding,embedding)
    UpperLimit = np.mean(D)
    idx = np.where(D!=0.0)
    LowerLimit = np.amin(D[idx])
    PossibleEpsilons = np.linspace(LowerLimit,UpperLimit+0.001,10)
    RPs = []
    RPEntropies = []

    for i in range(PossibleEpsilons.shape[0]):
      eps = PossibleEpsilons[i]
      rp = self.OptimumRP(em = embedding, eps = eps)
      RPs.append(rp)

      prob = self.RPHistogram(np.round(rp,2))
      entropy = self.CalculateEntropy(prob)
      RPEntropies.append(entropy)

    idx_max = np.where(RPEntropies==np.amax(RPEntropies))[0][0]
    OptRP = RPs[idx_max]
    return OptRP

