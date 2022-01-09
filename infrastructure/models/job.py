from sqlalchemy import Column,String,JSON,Integer,Date, Float, Time
from sqlalchemy.orm import relationship
from infrastructure.base_mixin import BaseMixin
from infrastructure.base_class import Base

class Job(BaseMixin,Base):
    detrack_type = Column(String, nullable=False)
    primary_job_status=Column(String)
    open_to_marketplace=Column(String)
    marketplace_offer=Column(String)
    do_number=Column(String,nullable=False)
    date=Column(Date,nullable=False)
    start_date=Column(Date)
    status=Column(String)
    job_release_time=Column(Time)
    job_time=Column(String)
    time_window=Column(String)
    job_received_date=Column(Date)
    tracking_number=Column(String)
    order_number=Column(String)
    job_type=Column(String)
    job_sequence=Column(String)
    job_fee=Column(String)
    address_lat=Column(String)
    address_lng=Column(String)
    address=Column(String ,nullable=False)
    company_name=Column(String)
    address_1=Column(String)
    address_2=Column(String)
    address_3=Column(String)
    postal_code=Column(String)
    city=Column(String)
    state=Column(String)
    country=Column(String)
    billing_address=Column(String)
    deliver_to_collect_from=Column(String)
    last_name=Column(String)
    phone_number=Column(String)
    sender_phone_number=Column(String)
    fax_number=Column(String)
    instructions=Column(String)
    assign_to=Column(String)
    notify_email=Column(String)
    webhook_url=Column(String)
    zone=Column(String)
    customer=Column(String)
    account_number=Column(String)
    job_owner=Column(String)
    invoice_number=Column(String)
    payment_mode=Column(String)
    payment_amount=Column(String)
    group_id=Column(String)
    group_name=Column(String)
    vendor_name=Column(String)
    source=Column(String)
    weight=Column(Integer)
    parcel_width=Column(Integer)
    parcel_length=Column(Integer)
    parcel_height=Column(Integer)
    cubic_meter=Column(Float)
    boxes=Column(Integer)
    cartons=Column(Integer)
    pieces=Column(Integer)
    envelopes=Column(Integer)
    pallets=Column(Integer)
    bins=Column(Integer)
    trays=Column(Integer)
    bundles=Column(Integer)
    rolls=Column(Integer)
    number_of_shipping_labels=Column(Integer)
    attachment_url=Column(String)
    carrier=Column(String)
    auto_reschedule=Column(String)
    eta_time=Column(Time)
    depot=Column(String)
    depot_contact=Column(String)
    department=Column(String)
    sales_person=Column(String)
    identification_number=Column(String)
    bank_prefix=Column(String)
    run_number=Column(String)
    pick_up_from=Column(String)
    pick_up_time=Column(String)
    pick_up_lat=Column(String)
    pick_up_lng=Column(String)
    pick_up_address=Column(String)
    pick_up_address_1=Column(String)
    pick_up_address_2=Column(String)
    pick_up_address_3=Column(String)
    pick_up_city=Column(String)
    pick_up_state=Column(String)
    pick_up_country=Column(String)
    pick_up_postal_code=Column(String)
    pick_up_zone=Column(String)
    job_price=Column(Float)
    insurance_price=Column(Float)
    insurance_coverage=Column(String)
    total_price=Column(Float)
    payer_type=Column(String)
    remarks=Column(String)
    service_type=Column(String)
    warehouse_address=Column(String)
    destination_time_window=Column(String)
    door=Column(String)
    time_zone=Column(String)
    vehicle_type=Column(String)
    items=relationship("JobItem",back_populates="job")
    pod_time=Column(Date)
    id=Column(String)
    job_age=Column(String)
    detrack_number=Column(String)
    tracking_status=Column(String)
    shipper_name=Column(String)
    reason=Column(String)
    last_reason=Column(String)
    received_by_sent_by=Column(String)
    note=Column(String)
    live_eta=Column(String)
    pod_lat=Column(String)
    pod_lng=Column(String)
    pod_address=Column(String)
    info_received_at=Column(Time)
    head_to_pick_up_at=Column(Time)
    pick_up_at=Column(Time)
    scheduled_at=Column(Time)
    at_warehouse_at=Column(Time)
    out_for_delivery_at=Column(Time)
    head_to_delivery_at=Column(Time)
    cancelled_at=Column(Time)
    pick_up_failed_count=Column(Time)
    deliver_failed_count=Column(Time)
    pick_up_assign_to=Column(Time)
    pick_up_reason=Column(Time)
    pod_at=Column(Time)
    texted_at=Column(Time)
    called_at=Column(Time)
    address_tracked_at=Column(Time)
    arrived_lat=Column(float)
    arrived_lng=Column(float)
    arrived_address=Column(String)
    arrived_at=Column(Time)
    serial_number=Column(String)
    signed_at=Column(Time)
    photo_1_at=Column(Time)
    photo_2_at=Column(Time)
    photo_3_at=Column(Time)
    photo_4_at=Column(Time)
    photo_5_at=Column(Time)
    photo_6_at=Column(Time)
    photo_7_at=Column(Time)
    photo_8_at=Column(Time)
    photo_9_at=Column(Time)
    photo_10_at=Column(Time)
    signature_file_url=Column(String)
    photo_1_file_url=Column(String)
    photo_2_file_url=Column(String)
    photo_3_file_url=Column(String)
    photo_4_file_url=Column(String)
    photo_5_file_url=Column(String)
    photo_6_file_url=Column(String)
    photo_7_file_url=Column(String)
    photo_8_file_url=Column(String)
    photo_9_file_url=Column(String)
    photo_10_file_url=Column(String)
    actual_weight=Column(Integer)
    temperature=Column(Integer)
    hold_time=Column(Integer)
    payment_collected=Column(Float)
    actual_crates=Column(Integer)
    actual_pallets=Column(Integer)
    actual_utilization=Column(Integer)
    attempt=Column(Integer)
    goods_service_rating=Column(Integer)
    driver_rating=Column(Integer)
    customer_feedback=Column(String)
    items_count=Column(Integer)
    tracking_link=Column(String)


    



    
    

   











