 **Psychotherapy System \- Doctor Panel API Endpoints**

![alt text](https://github.com/amirmahdi-chiti/Psychotherapy-System/blob/main/Screenshot%202024-06-11%20at%2019-30-33%20FastAPI%20-%20Swagger%20UI.png?raw=true)
**Authentication**

### **1\. Login**

*  **Endpoint:** POST /api/auth/login  
* **Description: Authenticate a doctor and return a JWT token.**  
* **Payload:**  
    **json**  
    **{**  
  	**"email": "doctor@example.com",**  
  	**"password": "password123"**  
    **}**

### **2\. Logout**

* **Endpoint:** `POST /api/auth/logout`  
* **Description:** Logout the authenticated doctor.  
* **Payload:** `None`


### **`3. Register`**

* **`Endpoint:`** `POST /api/auth/register`  
* **`Description:`** `Register a new doctor account.`  
* **`Payload:`**  
  **`{`**  
    **`"name": "Dr. Araban",`**  
    **`"email": "doctor@example.com",`**  
    **`"password": "password123"`**  
  **`}`**  
  


### **`4. Profile`**

* **`Endpoint: GET /api/auth/profile`**  
* **`Description: Get the authenticated doctor's profile.`**  
* **`Payload: None`**

## **`Patient Management`**

### **`1. Get All Patients`**

* **`Endpoint: GET /api/patients`**  
* **`Description: Retrieve a list of all patients.`**  
* **`Payload: None`**

### **`2. Get Patient by ID`**

* **`Endpoint: GET /api/patients/{patientId}`**  
* **`Description: Retrieve detailed information of a specific patient.`**  
* **`Payload: None`**

### **`3. Create New Patient`**

* **`Endpoint: POST /api/patients`**  
* **`Description: Add a new patient to the system.`**  
* **`Payload:`**  
  **`{`**  
    **`"name": "Jane Doe",`**  
    **`"dob": "1980-01-01",`**  
    **`"contactInfo": "123-456-7890",`**  
    **`"medicalHistory": "..."`**  
  **`}`**


### **`5. Delete Patient`**

* **`Endpoint: DELETE /api/patients/{patientId}`**  
* **`Description: Remove a patient from the system.`**  
* **`Payload: None`**

## **`Appointment Management`**

### **`1. Get All Appointments`**

* **`Endpoint: GET /api/appointments`**  
* **`Description: Retrieve all appointments.`**  
* **`Payload: None`**

### **`2. Get Appointments for a Doctor`**

* **`Endpoint: GET /api/appointments/doctor/{doctorId}`**  
* **`Description: Retrieve all appointments for a specific doctor.`**  
* **`Payload: None`**

### **`3. Get Appointments for a Patient`**

* **`Endpoint: GET /api/appointments/patient/{patientId}`**  
* **`Description: Retrieve all appointments for a specific patient.`**  
* **`Payload: None`**

### **`4. Create Appointment`**

* **`Endpoint: POST /api/appointments`**  
* **`Description: Schedule a new appointment.`**  
* **`Payload:`**  
  **`json`**  
  **`{`**  
    **`"doctorId": "123",`**  
    **`"patientId": "456",`**  
    **`"date": "2024-06-01",`**  
    **`"time": "10:00 AM",`**  
    **`"notes": "Initial consultation"`**  
  **`}`**  
* **`5. Update Appointment`**  
  * **`Endpoint: PUT /api/appointments/{appointmentId}`**  
  * **`Description: Modify details of an existing appointment.`**  
  * **`Payload:`**  
    **`json`**  
    **`{`**  
      **`"date": "2024-06-01",`**  
      **`"time": "11:00 AM",`**  
      **`"notes": "Rescheduled"`**  
    **`}`**  
  *   
* **`6. Delete Appointment`**  
  * **`Endpoint: DELETE /api/appointments/{appointmentId}`**  
  * **`Description: Cancel an appointment.`**  
  * **`Payload: None`**  
* **`Medical Records`**  
  **`1. Get Medical Records for a Patient`**  
  * **`Endpoint: GET /api/medical-records/patient/{patientId}`**  
  * **`Description: Retrieve medical records for a specific patient.`**  
  * **`Payload: None`**  
* **`2. Add Medical Record`**  
  * **`Endpoint: POST /api/medical-records`**  
  * **`Description: Add a new medical record for a patient.`**  
  * **`Payload:`**  
    **`json`**  
    **`{`**  
      **`"patientId": "456",`**  
      **`"record": "Patient is showing improvement..."`**  
    **`}`**  
  *   
* **`3. Update Medical Record`**  
  * **`Endpoint: PUT /api/medical-records/{recordId}`**  
  * **`Description: Update an existing medical record.`**  
  * **`Payload:`**  
    **`json`**  
    **`{`**  
      **`"record": "Updated notes on patient progress..."`**  
    **`}`**  
      
* **`4. Delete Medical Record`**  
  * **`Endpoint: DELETE /api/medical-records/{recordId}`**  
  * **`Description: Remove a medical record.`**  
  * **`Payload: None`**  
* **`Messaging and Notifications`**  
  **`1. Get Messages`**  
  * **`Endpoint: GET /api/messages`**  
  * **`Description: Retrieve all messages for the doctor.`**  
  * **`Payload: None`**  
* **`2. Send Message`**  
  * **`Endpoint: POST /api/messages`**  
  * **`Description: Send a new message to a patient or another doctor.`**  
  * **`Payload:`**  
    **`json`**  
    **`{`**  
      **`"recipientId": "456",`**  
      **`"message": "Your next appointment is scheduled..."`**  
    **`}`**  
  *   
* **`3. Get Notifications`**  
  * **`Endpoint: GET /api/notifications`**  
  * **`Description: Retrieve all notifications for the doctor.`**  
  * **`Payload: None`**  
* **`Billing and Invoicing`**  
  **`1. Get Invoices for a Patient`**  
  * **`Endpoint: GET /api/invoices/patient/{patientId}`**  
  * **`Description: Retrieve all invoices for a specific patient.`**  
  * **`Payload: None`**  
* **`2. Create Invoice`**  
  * **`Endpoint: POST /api/invoices`**  
  * **`Description: Create a new invoice for a patient.`**  
  * **`Payload:`**  
    **`json`**  
    **`{`**  
      **`"patientId": "456",`**  
      **`"amount": "100.00",`**  
      **`"description": "Consultation fee"`**  
    **`}`**  
  *   
* **`3. Update Invoice`**  
  * **`Endpoint: PUT /api/invoices/{invoiceId}`**  
  * **`Description: Update details of an existing invoice.`**  
  * **`Payload:`**  
    **`json`**  
    **`{`**  
      **`"amount": "120.00",`**  
      **`"description": "Updated fee"`**  
    **`}`**  
  *   
* **`4. Delete Invoice`**  
  * **`Endpoint: DELETE /api/invoices/{invoiceId}`**  
  * **`Description: Delete an invoice.`**  
  * **`Payload: None`**  
* **`Appointment Reservation`**  
  **`1. View Available Appointment Slots`**  
  * **`Endpoint: GET /api/appointments/available`**  
  * **`Description: Retrieve available appointment slots for a given date or date range.`**  
  * **`Query Parameters:`**  
    * **`date (optional): Specific date to check availability (e.g., 2024-06-01)`**  
    * **`startDate (optional): Start date of the range (e.g., 2024-06-01)`**  
    * **`endDate (optional): End date of the range (e.g., 2024-06-07)`**  
  * **`Response:`**  
    **`json`**  
    **`{`**  
      **`"availableSlots": [`**  
        **`{`**  
          **`"doctorId": "123",`**  
          **`"date": "2024-06-01",`**  
          **`"time": "10:00 AM"`**  
        **`},`**  
        **`{`**  
          **`"doctorId": "123",`**  
          **`"date": "2024-06-01",`**  
          **`"time": "11:00 AM"`**  
        **`}`**  
      **`]`**  
    **`}`**  
    


### **`2. Reserve an Appointment`**

* **`Endpoint: POST /api/appointments`**  
* **`Description: Reserve a new appointment slot for a patient.`**  
* **`Payload:`**  
  **`Json`**  
  **`{`**  
    **`"doctorId": "123",`**  
    **`"patientId": "456",`**  
    **`"date": "2024-06-01",`**  
    **`"time": "10:00 AM",`**  
    **`"reason": "Initial consultation"`**  
  **`}`**

	**`Response:`**

**`json`**

**`{`**

  **`"appointmentId": "789",`**

  **`"doctorId": "123",`**

  **`"patientId": "456",`**

  **`"date": "2024-06-01",`**

  **`"time": "10:00 AM",`**

  **`"reason": "Initial consultation",`**

  **`"status": "Confirmed"`**

**`}`**

* **`3. Update an Appointment Reservation`**  
  * **`Endpoint: PUT /api/appointments/{appointmentId}`**  
  * **`Description: Update the details of an existing appointment reservation.`**  
  * **`Payload:`**  
    **`json`**  
    **`{`**  
      **`"date": "2024-06-02",`**  
      **`"time": "11:00 AM",`**  
      **`"reason": "Follow-up consultation"`**  
    **`}`**

    
* **`Response:`**  
  **`json`**  
  **`{`**  
    **`"appointmentId": "789",`**  
    **`"doctorId": "123",`**  
    **`"patientId": "456",`**  
    **`"date": "2024-06-02",`**  
    **`"time": "11:00 AM",`**  
    **`"reason": "Follow-up consultation",`**  
    **`"status": "Updated"`**  
  **`}`**





[image1]: <data:image/png;base64,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>
