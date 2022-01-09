"""job

Revision ID: c340ada85473
Revises: 2613598563cb
Create Date: 2022-01-08 22:23:02.929897

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c340ada85473'
down_revision = '2613598563cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('detrack_type', sa.String(), nullable=False),
    sa.Column('primary_job_status', sa.String(), nullable=True),
    sa.Column('open_to_marketplace', sa.String(), nullable=True),
    sa.Column('marketplace_offer', sa.String(), nullable=True),
    sa.Column('do_number', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('job_release_time', sa.Time(), nullable=True),
    sa.Column('job_time', sa.String(), nullable=True),
    sa.Column('time_window', sa.String(), nullable=True),
    sa.Column('job_received_date', sa.Date(), nullable=True),
    sa.Column('tracking_number', sa.String(), nullable=True),
    sa.Column('order_number', sa.String(), nullable=True),
    sa.Column('job_type', sa.String(), nullable=True),
    sa.Column('job_sequence', sa.String(), nullable=True),
    sa.Column('job_fee', sa.String(), nullable=True),
    sa.Column('address_lat', sa.String(), nullable=True),
    sa.Column('address_lng', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=True),
    sa.Column('address_1', sa.String(), nullable=True),
    sa.Column('address_2', sa.String(), nullable=True),
    sa.Column('address_3', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('billing_address', sa.String(), nullable=True),
    sa.Column('deliver_to_collect_from', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('sender_phone_number', sa.String(), nullable=True),
    sa.Column('fax_number', sa.String(), nullable=True),
    sa.Column('instructions', sa.String(), nullable=True),
    sa.Column('assign_to', sa.String(), nullable=True),
    sa.Column('notify_email', sa.String(), nullable=True),
    sa.Column('webhook_url', sa.String(), nullable=True),
    sa.Column('zone', sa.String(), nullable=True),
    sa.Column('customer', sa.String(), nullable=True),
    sa.Column('account_number', sa.String(), nullable=True),
    sa.Column('job_owner', sa.String(), nullable=True),
    sa.Column('invoice_number', sa.String(), nullable=True),
    sa.Column('payment_mode', sa.String(), nullable=True),
    sa.Column('payment_amount', sa.String(), nullable=True),
    sa.Column('group_id', sa.String(), nullable=True),
    sa.Column('group_name', sa.String(), nullable=True),
    sa.Column('vendor_name', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('parcel_width', sa.Integer(), nullable=True),
    sa.Column('parcel_length', sa.Integer(), nullable=True),
    sa.Column('parcel_height', sa.Integer(), nullable=True),
    sa.Column('cubic_meter', sa.Float(), nullable=True),
    sa.Column('boxes', sa.Integer(), nullable=True),
    sa.Column('cartons', sa.Integer(), nullable=True),
    sa.Column('pieces', sa.Integer(), nullable=True),
    sa.Column('envelopes', sa.Integer(), nullable=True),
    sa.Column('pallets', sa.Integer(), nullable=True),
    sa.Column('bins', sa.Integer(), nullable=True),
    sa.Column('trays', sa.Integer(), nullable=True),
    sa.Column('bundles', sa.Integer(), nullable=True),
    sa.Column('rolls', sa.Integer(), nullable=True),
    sa.Column('number_of_shipping_labels', sa.Integer(), nullable=True),
    sa.Column('attachment_url', sa.String(), nullable=True),
    sa.Column('carrier', sa.String(), nullable=True),
    sa.Column('auto_reschedule', sa.String(), nullable=True),
    sa.Column('eta_time', sa.Time(), nullable=True),
    sa.Column('depot', sa.String(), nullable=True),
    sa.Column('depot_contact', sa.String(), nullable=True),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('sales_person', sa.String(), nullable=True),
    sa.Column('identification_number', sa.String(), nullable=True),
    sa.Column('bank_prefix', sa.String(), nullable=True),
    sa.Column('run_number', sa.String(), nullable=True),
    sa.Column('pick_up_from', sa.String(), nullable=True),
    sa.Column('pick_up_time', sa.String(), nullable=True),
    sa.Column('pick_up_lat', sa.String(), nullable=True),
    sa.Column('pick_up_lng', sa.String(), nullable=True),
    sa.Column('pick_up_address', sa.String(), nullable=True),
    sa.Column('pick_up_address_1', sa.String(), nullable=True),
    sa.Column('pick_up_address_2', sa.String(), nullable=True),
    sa.Column('pick_up_address_3', sa.String(), nullable=True),
    sa.Column('pick_up_city', sa.String(), nullable=True),
    sa.Column('pick_up_state', sa.String(), nullable=True),
    sa.Column('pick_up_country', sa.String(), nullable=True),
    sa.Column('pick_up_postal_code', sa.String(), nullable=True),
    sa.Column('pick_up_zone', sa.String(), nullable=True),
    sa.Column('job_price', sa.Float(), nullable=True),
    sa.Column('insurance_price', sa.Float(), nullable=True),
    sa.Column('insurance_coverage', sa.String(), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('payer_type', sa.String(), nullable=True),
    sa.Column('remarks', sa.String(), nullable=True),
    sa.Column('service_type', sa.String(), nullable=True),
    sa.Column('warehouse_address', sa.String(), nullable=True),
    sa.Column('destination_time_window', sa.String(), nullable=True),
    sa.Column('door', sa.String(), nullable=True),
    sa.Column('time_zone', sa.String(), nullable=True),
    sa.Column('vehicle_type', sa.String(), nullable=True),
    sa.Column('pod_time', sa.Time(), nullable=True),
    sa.Column('created_user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('updated_user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['created_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['updated_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jobitem',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('sku', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('purchase_order_number', sa.String(), nullable=True),
    sa.Column('batch_number', sa.String(), nullable=True),
    sa.Column('expiry_date', sa.Date(), nullable=True),
    sa.Column('comments', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('unit_of_measure', sa.String(), nullable=True),
    sa.Column('checked', sa.Boolean(), nullable=True),
    sa.Column('actual_quantity', sa.Integer(), nullable=True),
    sa.Column('inbound_quantity', sa.Integer(), nullable=True),
    sa.Column('unload_time_estimate', sa.String(), nullable=True),
    sa.Column('unload_time_actual', sa.String(), nullable=True),
    sa.Column('follow_up_quantity', sa.Integer(), nullable=True),
    sa.Column('follow_up_reason', sa.String(), nullable=True),
    sa.Column('rework_quantity', sa.Integer(), nullable=True),
    sa.Column('rework_reason', sa.String(), nullable=True),
    sa.Column('reject_quantity', sa.Integer(), nullable=True),
    sa.Column('reject_reason', sa.String(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('serial_numbers', sa.JSON(), nullable=True),
    sa.Column('job_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('updated_user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['created_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.ForeignKeyConstraint(['updated_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobitem')
    op.drop_table('job')
    # ### end Alembic commands ###