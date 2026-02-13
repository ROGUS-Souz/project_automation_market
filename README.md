🤖 ERP Protein Entry Automation (RPA)

[PT-BR] Resumo do Projeto: Sistema de automação robótica de processos (RPA) desenvolvido em Python para automatizar o lançamento de registros de proteínas (bovinos, suínos, aves e pescados) em sistema ERP (Enterprise Resource Planning). O script substitui a digitação manual, interagindo diretamente com a interface gráfica do software. Impacto Real: Redução do tempo de lançamento de 10 minutos para 4 minutos por lote, gerando um **ganho de 60% em eficiência operacional e eliminando erros de digitação.**

📝 Description

A Python-based RPA tool designed to streamline the administrative task of protein inventory registration. By using GUI automation, the script navigates through ERP menus, selects cost centers, and inputs product quantities from a structured data dictionary.

🎯 Objective

To eliminate repetitive manual data entry in the ERP system, ensuring faster processing times and 100% data integrity during the transition from physical records to the digital database.

⚙️ Main Features

GUI Interaction: Precise mouse and keyboard automation using PyAutoGUI.

Dynamic Context Logic: Automatically identifies and fills "Cost Centers" based on the entry type (Event, Team, Construction, etc.).

Smart Iteration: Processes a wide range of protein categories (Bovines, Poultry, Swine, Fish) using Python iterators.

Execution Control: Synchronized wait times to match the ERP’s response speed, preventing system crashes.

🛠️ Technologies Used

Python: Main programming language.

PyAutoGUI: For graphical user interface automation (clicks, typing, and navigation).

Time: For process synchronization and interval management.

Itertools/Collections: To manage and iterate through product databases.

📋 Process Flow

Initialization: Script triggers the ERP's "Add" function.

Context Definition: Selection of the specific event type (e.g., "Evento - Proteína").

Cost Center Mapping: Automatic input of the corresponding cost center code.

Product Loop: The script iterates through a dictionary containing products and quantities.

Validation: Automatic confirmation of each entry.

Finalization: System ready for the next batch.

📊 Generated Outputs & Impact

Productivity Increase: Task completed 60% faster than manual entry.

Error Rate: Reduced to 0% by eliminating human fatigue in repetitive typing.

Standardization: All entries follow the exact same naming and categorization convention.

💡 Benefits

Time Saving: Frees up the analyst for higher-value tasks (like data analysis).

Scalability: Can be easily adapted to include new products or other ERP modules.

Reliability: Guarantees that the stock in the system perfectly matches the provided data.

👥 Target Audience

Administrative assistants, quality control analysts, and warehouse managers dealing with high volumes of manual data entry.
