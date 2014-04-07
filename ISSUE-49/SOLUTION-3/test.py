from easter import western, orthodox

def test():
	assert western(1583) == (10,4,1583)
	assert western(1710) == (20,4,1710)
	assert western(1868) == (12,4,1868)
	assert western(1936) == (12,4,1936)
	assert western(1994) == (3,4,1994)
	assert western(1995) == (16,4,1995)
	assert western(1996) == (7,4,1996)
	assert western(1997) == (30,3,1997)
	assert western(1998) == (12,4,1998)
	assert western(1999) == (4,4,1999)
	assert western(2000) == (23,4,2000)
	assert western(2001) == (15,4,2001)
	assert western(2002) == (31,3,2002)
	assert western(2003) == (20,4,2003)
	assert western(2004) == (11,4,2004)
	assert western(2005) == (27,3,2005)
	assert western(2006) == (16,4,2006)
	assert western(2007) == (8,4,2007)
	assert western(2008) == (23,3,2008)
	assert western(2009) == (12,4,2009)
	assert western(2010) == (4,4,2010)
	assert western(2011) == (24,4,2011)
	assert western(2012) == (8,4,2012)
	assert western(2013) == (31,3,2013)
	assert western(2014) == (20,4,2014)
	assert western(2015) == (5,4,2015)
	assert western(2016) == (27,3,2016)
	assert western(2017) == (16,4,2017)
	assert western(2018) == (1,4,2018)
	assert western(2019) == (21,4,2019)
	assert western(2020) == (12,4,2020)
	assert western(2021) == (4,4,2021)
	assert western(2022) == (17,4,2022)
	assert western(2023) == (9,4,2023)
	assert western(2024) == (31,3,2024)
	assert western(2025) == (20,4,2025)
	assert western(2026) == (5,4,2026)
	assert western(2027) == (28,3,2027)
	assert western(2028) == (16,4,2028)
	assert western(2029) == (1,4,2029)
	assert western(2030) == (21,4,2030)
	assert western(2031) == (13,4,2031)
	assert western(2032) == (28,3,2032)
	assert western(2033) == (17,4,2033)
	assert western(2034) == (9,4,2034)
	assert western(2098) == (20,4,2098)
	assert western(2161) == (12,4,2161)
	assert western(2298) == (3,4,2298)
	assert orthodox(1583) == (10,4,1583)
	assert orthodox(1994) == (1,5,1994)
	assert orthodox(1995) == (23,4,1995)
	assert orthodox(1996) == (14,4,1996)
	assert orthodox(1997) == (27,4,1997)
	assert orthodox(1998) == (19,4,1998)
	assert orthodox(1999) == (11,4,1999)
	assert orthodox(2000) == (30,4,2000)
	assert orthodox(2001) == (15,4,2001)
	assert orthodox(2002) == (5,5,2002)
	assert orthodox(2003) == (27,4,2003)
	assert orthodox(2004) == (11,4,2004)
	assert orthodox(2005) == (1,5,2005)
	assert orthodox(2006) == (23,4,2006)
	assert orthodox(2007) == (8,4,2007)
	assert orthodox(2008) == (27,4,2008)
	assert orthodox(2009) == (19,4,2009)
	assert orthodox(2010) == (4,4,2010)
	assert orthodox(2011) == (24,4,2011)
	assert orthodox(2012) == (15,4,2012)
	assert orthodox(2013) == (5,5,2013)
	assert orthodox(2014) == (20,4,2014)
	assert orthodox(2015) == (12,4,2015)
	assert orthodox(2016) == (1,5,2016)
	assert orthodox(2017) == (16,4,2017)
	assert orthodox(2018) == (8,4,2018)
	assert orthodox(2019) == (28,4,2019)
	assert orthodox(2020) == (19,4,2020)
	assert orthodox(2021) == (2,5,2021)
	assert orthodox(2022) == (24,4,2022)
	assert orthodox(2023) == (16,4,2023)
	assert orthodox(2024) == (5,5,2024)
	assert orthodox(2025) == (20,4,2025)
	assert orthodox(2026) == (12,4,2026)
	assert orthodox(2027) == (2,5,2027)
	assert orthodox(2028) == (16,4,2028)
	assert orthodox(2029) == (8,4,2029)
	assert orthodox(2030) == (28,4,2030)
	assert orthodox(2031) == (13,4,2031)
	assert orthodox(2032) == (2,5,2032)
	assert orthodox(2033) == (24,4,2033)
	assert orthodox(2034) == (9,4,2034)
	print "All tests passed"

test()
