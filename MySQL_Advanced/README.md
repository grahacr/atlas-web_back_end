Learning more MySQL!
Learning Objectives:

- How to create tables with constraints
- How to optimize queries by adding indexes
- - What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL


# Create the database (if it doesn't already exist)
mysql -uroot -p -e "CREATE DATABASE holberton;"

# Import the data into the database
mysql -uroot -p holberton < metal_bands.sql

# Execute your ranking script
cat rank_bands.sql | mysql -uroot -p holberton > tmp_res

# Select results from the ranked_bands table
echo "SELECT * FROM ranked_bands;" | mysql -uroot -p holberton > tmp_res

# View the output
head tmp_res
