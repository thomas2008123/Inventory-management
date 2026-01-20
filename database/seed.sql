INSERT INTO Items
(Name, Description, InStock, Price, StockAmount, Rating, DeliveryDate, ItemType)
VALUES
-- Electronics
('Laptop', 'High-performance laptop with 16GB RAM and 512GB SSD', 1, 999.99, 10, 4.5, '2025-12-01', 'Electronics'),
('Smartphone', 'Latest model smartphone with advanced camera features', 1, 799.99, 20, 4.7, '2025-11-15', 'Electronics'),
('Tablet', '10-inch tablet ideal for work and entertainment', 1, 499.99, 15, 4.3, '2025-11-20', 'Electronics'),
('Gaming Console', 'Next-gen console with ultra-fast SSD', 1, 599.99, 8, 4.8, '2025-12-10', 'Electronics'),
('Smartwatch', 'Fitness-focused smartwatch with heart-rate monitoring', 1, 249.99, 25, 4.4, '2025-10-30', 'Electronics'),

-- Accessories
('Headphones', 'Noise-cancelling over-ear headphones', 1, 199.99, 30, 4.2, '2025-10-20', 'Accessories'),
('Wireless Mouse', 'Ergonomic wireless mouse with adjustable DPI', 1, 49.99, 50, 4.1, '2025-10-05', 'Accessories'),
('Mechanical Keyboard', 'RGB mechanical keyboard with blue switches', 1, 129.99, 40, 4.6, '2025-10-12', 'Accessories'),
('USB-C Hub', 'Multi-port USB-C hub with HDMI and Ethernet', 1, 79.99, 35, 4.0, '2025-10-18', 'Accessories'),

-- Office
('Office Chair', 'Ergonomic office chair with lumbar support', 1, 299.99, 12, 4.3, '2025-11-05', 'Office'),
('Standing Desk', 'Height-adjustable standing desk', 1, 499.99, 6, 4.6, '2025-11-25', 'Office'),
('Desk Lamp', 'LED desk lamp with adjustable brightness', 1, 39.99, 45, 4.0, '2025-09-30', 'Office'),

-- Home
('Air Purifier', 'HEPA air purifier for large rooms', 1, 229.99, 18, 4.4, '2025-11-10', 'Home'),
('Coffee Maker', 'Automatic coffee maker with programmable timer', 1, 149.99, 22, 4.2, '2025-10-28', 'Home'),
('Vacuum Cleaner', 'Bagless vacuum cleaner with strong suction', 1, 199.99, 14, 4.3, '2025-11-02', 'Home'),

-- Out of stock examples
('External Hard Drive', '2TB portable external hard drive', 0, 99.99, 0, 4.5, '2025-12-15', 'Accessories'),
('Router', 'Wi-Fi 6 high-speed wireless router', 0, 179.99, 0, 4.6, '2025-12-20', 'Electronics');


INSERT INTO TechnicalDetails
(ItemID, Weight, Dimensions, Supplier, Manufacturer)
VALUES
(1, 2.5, '35x24x2 cm', 'TechSupplier Inc.', 'TechBrand Ltd.'),
(2, 0.2, '15x7x0.8 cm', 'MobileSuppliers Co.', 'SmartTech Corp.'),
(3, 0.6, '25x16x0.7 cm', 'TabletWorld', 'TabTech'),
(4, 3.2, '39x26x8 cm', 'GameSupply Ltd.', 'NextGen Gaming'),
(5, 0.05, '4x4x1 cm', 'WearableHub', 'FitLife'),

(6, 0.3, '20x18x8 cm', 'AudioExperts Ltd.', 'SoundMasters Inc.'),
(7, 0.09, '11x6x3 cm', 'PeriphCo', 'ClickPro'),
(8, 1.1, '44x14x4 cm', 'Keyboards Inc.', 'TypeFast'),
(9, 0.15, '12x5x2 cm', 'HubWorks', 'Connectix'),

(10, 18.0, '70x70x120 cm', 'OfficeWorld', 'ErgoComfort'),
(11, 32.0, '140x70x75 cm', 'DeskMakers', 'LiftDesk'),
(12, 1.2, '40x15x15 cm', 'LightCo', 'BrightLite'),

(13, 5.5, '45x25x25 cm', 'HomeAir Ltd.', 'PureBreath'),
(14, 3.0, '30x20x25 cm', 'CoffeeSupplies', 'BrewMaster'),
(15, 6.8, '50x30x30 cm', 'CleanHome', 'DustAway'),

(16, 0.25, '12x8x2 cm', 'StoragePlus', 'DataSafe'),
(17, 0.4, '22x16x4 cm', 'NetSuppliers', 'FastLink');


INSERT INTO Reviews
(ItemID, Rating, Comment)
VALUES
(1, 5, 'Excellent performance and build quality!'),
(1, 4, 'Very fast but a bit expensive.'),

(2, 4, 'Great camera but battery life could be better.'),
(2, 5, 'Best phone I have owned so far.'),

(3, 4, 'Perfect size for reading and browsing.'),
(4, 5, 'Amazing graphics and fast load times.'),

(5, 4, 'Tracks workouts accurately.'),

(6, 4, 'Comfortable with good noise cancellation.'),
(6, 3, 'Sound is good but could be louder.'),

(8, 5, 'Fantastic typing experience.'),

(10, 4, 'Very comfortable for long work days.'),

(11, 5, 'Standing desk has improved my posture.'),

(13, 4, 'Air quality noticeably improved.'),

(14, 5, 'Makes great coffee quickly.'),

(15, 4, 'Strong suction and easy to clean.');
