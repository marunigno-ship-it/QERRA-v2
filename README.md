# QERRA-v2

**Hybrid Quantum-Classical Ethical Decision Engine** for humanoid robots and high-stakes AI.

## License
**AGPL-3.0**  
This project is licensed under the GNU Affero General Public License v3.0.  
See the [LICENSE](LICENSE) file for full details.

## System Architecture

```mermaid
flowchart TD
    A[Input: Robot sensor data / Query] --> B[Quantum Layer<br>W-state simulation]
    B --> C[Ethical Vectors<br>SEMEV-12 real-life based]
    C --> D[Toxicity & Manipulation Detector]
    D --> E[Safety Kernel<br>Region-aware override EU/USA/UAE]
    E --> F[Final Decision + Explanation]
    F --> G[Output: Robot action / Safe state]
