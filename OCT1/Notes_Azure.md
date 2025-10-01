Microsoft Azure – Resource Management
1. User Actions

Users create multiple resources in Azure (VMs, Databases, Storage, etc.).

These resources must be organized and managed properly.

2. Azure Portal / API

Azure Portal → GUI (Graphical interface) for creating & managing resources.

API → Programmatic access to create/manage resources.

3. Orchestrator

Acts like a manager/brain.

Coordinates all requests coming from Azure Portal or API.

Ensures resources are created, updated, or deleted correctly.

4. Fabric Controller

Heart of Azure’s infrastructure.

Runs on clusters of servers.

Responsible for:

Allocating physical resources (CPU, memory, networking).

Monitoring health of resources.

Restarting/replacing failed resources automatically.

Think of it as the control system for the data center.

5. How it Works (Flow)

User → creates request (via Portal/API).

Orchestrator → sends the request to Fabric Controller.

Fabric Controller → provisions and manages the actual resources on servers.

Fabric Controller keeps checking health and availability.

Summary:

User: Creates resources.

Azure Portal/API: Interfaces to request resources.

Orchestrator: Directs the requests.

Fabric Controller: Executes and manages resources on physical servers.
