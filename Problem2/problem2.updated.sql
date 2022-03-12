SELECT 
	d.name, e1.name,e1.salary 
	from
	employee e1
	join
	department d on e1.departmentid = d.id
where 
	3>(SELECT Count(DISTINCT e2.salary)
	  	from employee e2
	   where e2.salary >e1.salary
	   	and e1.departmentid = e2.departmentid
	  ) order by d.name
