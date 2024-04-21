import cirq
from cirq import Circuit, Simulator

def coin_flip():
  """Simulates a coin flip using a quantum circuit with measurement.
  Returns:
      str: "Heads" or "Tails" based on the random outcome.
  """
  # Create a qubit to represent the coin state
  qubit = cirq.LineQubit(0)

  # Create a circuit with a random bit flip operation
  circuit = Circuit()
  circuit.append(cirq.H(qubit))
  circuit.append(cirq.measure(qubit))
  

  # Simulate the circuit
  simulator = Simulator()
  result = simulator.run(circuit, repetitions=1)
  if result.measurements['q(0)'][0] == [0]:
    return "Heads"
  else:
    return "Tails"
