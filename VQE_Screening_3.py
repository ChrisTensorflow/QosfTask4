
# coding: utf-8

# # VQE Screening 3

# In[1]:


scaffold_codeBell = """

// Ref[2] https://www.asc.ohio-state.edu/perry.6/p5501_sp17/articles/quantum_gates.pdf
// Ref[3] https://arxiv.org/pdf/1901.00015.pdf

const double alpha0 = 3.14159265359;

module initialRotations(qbit reg[2]) {
  H(reg[0]); // Start of Fig. 3(a) of Ref[3]
  X(reg[1]); // Start of Fig. 2.29 of Ref[2] with A = B = X and C = an X-rotation by alpha0
  CNOT(reg[0], reg[1]); 
  X(reg[1]); 
  CNOT(reg[0], reg[1]); 
  Rx(reg[1], alpha0); // End of Fig. 2.29 of Ref[2] 
  CNOT(reg[1], reg[2]);
  H(reg[1]);
  S(reg[0]); 
  H(reg[0]); // End of Fig. 3(a) of Ref[3]
  
}

module entangler(qbit reg[2]) {
  H(reg[1]);
  CNOT(reg[1], reg[2]);

  H(reg[2]);
  CNOT(reg[2], reg[1]);
}


module prepareAnsatz(qbit reg[2]) {
  initialRotations(reg);
  entangler(reg);
}

module measure(qbit reg[2], cbit result[2]) {
  CNOT(reg[1], reg[2]);
  H(reg[1]);
  result[0] = MeasZ(reg[0]);
  result[1] = MeasZ(reg[1]);
  result[2] = MeasZ(reg[2]);
}

int main() {
  qbit reg[3];
  cbit result[3];

  prepareAnsatz(reg);
  measure(reg, result);

  return 0;
}


"""


# ***

# # Executing it!

# In[2]:


# Compile the Scaffold to OpenQASM
from scaffcc_interface import ScaffCC
openqasmBell = ScaffCC(scaffold_codeBell).get_openqasm()
print(openqasmBell)


# ### Execute on a Simulator

# In[3]:


from qiskit import Aer,QuantumCircuit, execute
Aer.backends()


# In[4]:


simulator = Aer.get_backend('qasm_simulator')
vqe_circBell = QuantumCircuit.from_qasm_str(openqasmBell)
num_shots = 100000
sim_resultBell = execute(vqe_circBell, simulator, shots=num_shots).result()

countsBell = sim_resultBell.get_counts()

expected_valueBellXX = (+countsBell.get('000', 0) - countsBell.get('001', 0) + countsBell.get('010', 0) - countsBell.get('011', 0) - countsBell.get('100', 0) + countsBell.get('101', 0) - countsBell.get('110', 0) + countsBell.get('111', 0)) / num_shots
expected_valueBellYY = (-countsBell.get('000', 0) + countsBell.get('001', 0) + countsBell.get('010', 0) - countsBell.get('011', 0) + countsBell.get('100', 0) - countsBell.get('101', 0) - countsBell.get('110', 0) + countsBell.get('111', 0)) / num_shots
expected_valueBellZZ = (+countsBell.get('000', 0) + countsBell.get('001', 0) - countsBell.get('010', 0) - countsBell.get('011', 0) - countsBell.get('100', 0) - countsBell.get('101', 0) + countsBell.get('110', 0) + countsBell.get('011', 0)) / num_shots

expected_value = 0.5 - 0.5 * expected_valueBellXX - 0.5 * expected_valueBellYY + 0.5 * expected_valueBellZZ 
print('The gives the derivative of the lowest eigenvalue with respect to alpha0, which is : %s' % expected_value)

#print(countsBell.get('00', 0))
#print(countsBell.get('01', 0))
#print(countsBell.get('10', 0))
#print(countsBell.get('11', 0))

#print(expected_valueBellXX)
#print(expected_valueBellYY)
#print(expected_valueBellZZ)


# ***

# # Circuit Visualization 

# In[5]:


from qiskit.tools.visualization import circuit_drawer
circuit_drawer(vqe_circBell, scale=.4)

