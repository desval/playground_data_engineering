-- Drop table if it exists
drop table if exists employee_salary;

-- Create the bitemporal table
create table employee_salary (
    employee_id int,
    salary decimal(10, 2),
    system_start_time timestamp not null,
    system_end_time timestamp not null,
    valid_start_time date not null,
    valid_end_time date not null,
    primary key (employee_id, system_start_time)
);

-- Insert sample data
insert into employee_salary (employee_id, salary, system_start_time, system_end_time, valid_start_time, valid_end_time)
values
    (1, 50000.00, '2025-01-01 09:00:00', '2025-01-10 12:00:00', '2025-01-01', '2025-12-31'),
    (1, 55000.00, '2025-01-10 12:00:00', '9999-12-31 23:59:59', '2025-06-01', '9999-12-31');

-- Query current data
select * 
from employee_salary
where system_end_time = '9999-12-31 23:59:59';

-- Query data valid for a specific real-world time
select * 
from employee_salary
where '2025-07-01' between valid_start_time and valid_end_time;

-- Update to reflect a salary change
update employee_salary
set system_end_time = current_timestamp
where employee_id = 1
  and system_end_time = '9999-12-31 23:59:59';

insert into employee_salary (employee_id, salary, system_start_time, system_end_time, valid_start_time, valid_end_time)
values
    (1, 60000.00, current_timestamp, '9999-12-31 23:59:59', '2025-06-01', '9999-12-31');
