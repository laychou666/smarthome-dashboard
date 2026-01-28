CREATE TABLE sensors (id SERIAL PRIMARY KEY, name TEXT, type TEXT, location TEXT);
CREATE TABLE sensor_data (time TIMESTAMPTZ NOT NULL, sensor_id INT REFERENCES sensors(id), value DOUBLE PRECISION);
SELECT create_hypertable('sensor_data', 'time');
