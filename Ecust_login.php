<?php
date_default_timezone_get("Asia/Chongqing");
$EcustID = "";//填入学号
$EcustPW = "";//填入密码（jwc的）
$EcustID = "10142045";
$EcustPW = "10142045";

if (($EcustID == "") && ($EcustPW == "")) {
	$EcustID = $_GET['id'];
	$EcustPW = $_GET['pw'];

}



// 
// $function_num = $_GET['func'];

class Ecust{
	public $curlobj;
	public $html;

	public $name; // 个人信息->姓名
	public $phone; // 个人信息->手机 （未获取）
	public $gender; // 个人信息->姓别
	public $dorm; // 个人信息->寝室
	public $class; // 个人信息->班级
	public $major; // 个人信息->专业
	public $department; // 个人信息->学院
	public $timeOfEnrollment; // 个人信息->入学时间

	//public $success = false;
	public function __construct($EcustID,$EcustPW){
		// 发送Post并获取Cookie：Start
		$data="__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTU1MjMxMzE0NA9kFgICAQ9kFgICBg8PFgIeBFRleHQFYOavm%2BiwpuaYguWQjOWtpu%2B8jOaCqOWlve%2B8geaCqOWujOaIkOacrOWtpuacn%2BeahOaVmeWtpua1i%2BivhO%2B8jOaJjeiDveeci%2BWIsOacrOWtpuacn%2BeahOaIkOe7qeOAgmRkZF%2FuvXV8GM900SI%2B8zKgZKNfA%2FTH&TxtStudentId=".$EcustID."&TxtPassword=".$EcustPW."&BtnLogin=%E7%99%BB%E5%BD%95&__EVENTVALIDATION=%2FwEWBAKog665AQK%2Fycb4AQLVqbaRCwLi44eGDLF4ZYE%2FPlBcalTxIVf0yprdM0lE";
		$this->curlobj = curl_init();
		curl_setopt($this->curlobj,CURLOPT_URL, 'http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentQueryLogin.aspx');
		curl_setopt($this->curlobj, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($this->curlobj,CURLOPT_COOKIESESSION,true);
		curl_setopt($this->curlobj,CURLOPT_COOKIEFILE,"cookiefile");
		curl_setopt($this->curlobj,CURLOPT_COOKIEJAR,"cookiefile");
		curl_setopt($this->curlobj, CURLOPT_COOKIE, session_name()."=".session_id());
		curl_setopt($this->curlobj, CURLOPT_HEADER, 0);
		curl_setopt($this->curlobj, CURLOPT_FOLLOWLOCATION, 1);

		curl_setopt($this->curlobj,CURLOPT_POST,1);
		curl_setopt($this->curlobj,CURLOPT_POSTFIELDS,$data);
		curl_setopt($this->curlobj, CURLOPT_HTTPHEADER, array("application/x-www-form-urlencoded;charset=utf-8",
			"Content-length:".strlen($data)
			));
		curl_exec($this->curlobj);
		// 发送Post并获取Cookie：End

		// 检验是否成功（实际没卵用）：Start
		curl_setopt($this->curlobj,CURLOPT_URL,"http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentQueryLeft.aspx");
		curl_setopt($this->curlobj,CURLOPT_POST,0);
		curl_setopt($this->curlobj,CURLOPT_HTTPHEADER,array("Content-type: text/xml"));
		$opt=curl_exec($this->curlobj);
		//curl_close($this->curlobj);
		//echo $opt;

		if (strpos($opt,"您好") !== false){
			$this->success = true ;
			echo "Suceess Login";
		}
		else {
			
			$this->success = false;
		}
		// 检验是否成功（实际没卵用）：End
		
		
		// 初始化 个人信息
		curl_setopt($this->curlobj,CURLOPT_URL,"http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentInformationDetail.aspx?key=0");
		$opt=curl_exec($this->curlobj);
		$this->html = new DOMDocument();
		$html_source = str_replace("gb2312" , "utf-8" ,$opt);
		@$this->html->loadHTML($html_source);
		$this->html->validateOnParse = true;
		$arrayPersonInfo =new ArrayObject(array());
		foreach ( $this->html->getElementsByTagName("input") as $key){
			$arrayPersonInfo->append($key->getAttribute("value"));
		}
		$this->name = $arrayPersonInfo[17];
		$this->gender = $arrayPersonInfo[13];
		$this->dorm = $arrayPersonInfo[27];
		$this->class = $arrayPersonInfo[5];
		$this->major = $arrayPersonInfo[4];
		$this->department = $arrayPersonInfo[29];
		$this->timeOfEnrollment = $arrayPersonInfo[32];



		//echo $name;

		
	}


	public function curl_POST($url,$data){
		/**
		 * 方便Post用
		 * 
		 */
		curl_setopt($this->curlobj,CURLOPT_URL, $url);
		curl_setopt($this->curlobj, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($this->curlobj,CURLOPT_COOKIESESSION,true);
		curl_setopt($this->curlobj,CURLOPT_COOKIEFILE,"cookiefile");
		curl_setopt($this->curlobj,CURLOPT_COOKIEJAR,"cookiefile");
		curl_setopt($this->curlobj, CURLOPT_COOKIE, session_name()."=".session_id());
		curl_setopt($this->curlobj, CURLOPT_HEADER, 0);
		curl_setopt($this->curlobj, CURLOPT_FOLLOWLOCATION, 1);

		curl_setopt($this->curlobj,CURLOPT_POST,1);
		curl_setopt($this->curlobj,CURLOPT_POSTFIELDS,$data);
		curl_setopt($this->curlobj, CURLOPT_HTTPHEADER, array("application/x-www-form-urlencoded;charset=utf-8",
			"Content-length:".strlen($data)
			));
		$opt = curl_exec($this->curlobj);
		return $opt;
		//curl_close($this->curlobj);
	}


	public function changePW($newPW){
		$data = "__VIEWSTATE=%2FwEPDwUKMTYzMjI1NzMyN2Rk6a%2BHx5mRWLuy0dJqc2wHB2274JE%3D&txtNewPwd1=".$newPW."&txtNewPwd2=".$newPW."&BtnOK=%E6%8F%90%E4%BA%A4&__EVENTVALIDATION=%2FwEWBAKll4qhCgL7mJ6BBAL7mJqBBAL9mpmPAVpXeLI7SJ4Gqk%2BqA%2BCwBw1nWJFC";
		$url = "http://202.120.108.14/ecustedu/StudentChangePassword.aspx";
		$this->curl_POST($url,$data);

	}


	public function XuanKeXinXi($year,$term){

		/**
		 * year 年份 例如1996 2014（只能填在校时间！
		 * term 学期 1（上学期）或2（下学期）
		 * 
		 */
		$data = "__VIEWSTATE=%2FwEPDwUKMTM4MjMzNDI4NQ9kFgICAQ9kFgQCAw8QDxYGHg1EYXRhVGV4dEZpZWxkBQhZZWFyVGVybR4ORGF0YVZhbHVlRmllbGQFCFllYXJUZXJtHgtfIURhdGFCb3VuZGdkEBUCBTIwMTQxBTIwMTQyFQIFMjAxNDEFMjAxNDIUKwMCZ2dkZAIJDzwrAAsAZGSMX4%2FWtLgBIQKKTJKe0kctZawz%2Bg%3D%3D&drpdwn_YearTerm=".$year.$term."&bttn_search=%E6%9F%A5%E8%AF%A2&__EVENTVALIDATION=%2FwEWBAKers%2B8CQKkoPSnBgKroPSnBgK1man8CWwzHLXGvjcGP5XoZl2avsaU%2BolS";
		$url = "http://202.120.108.14/ecustedu/E_SelectCourse/ScInFormation/syllabusHistory.aspx";
		$opt = $this->curl_POST($url,$data);
		//通过切割截取数据（官网太丑= =
		//
		//如果有人看不下去可以正则重写一下。。。
		//
		//echo $opt;
		$part_1_Array = explode("<tr class=\"headcenter\" bgcolor=\"#6699FF\">" , $opt);
		//echo $part_1_Array[0]."cut here";
		//echo $part_1_Array[1];
		$part_2_Array = explode("</table></td>", $part_1_Array[1]);
		//var_dump($part_2_Array);
		$table = str_replace(" class=\"griditem\" onmouseout=\"javascript:this.style.backgroundColor='#dedfde';\" onmouseover=\"javascript:this.style.backgroundColor='#fff7ce';cursor='hand';\"", "", $part_2_Array[0]);
		$table = str_replace(" class=\"gridalteritem\" onmouseout=\"javascript:this.style.backgroundColor='#ffffff';\" onmouseover=\"javascript:this.style.backgroundColor='#fff7ce';cursor='hand';\"" , "" , $table);
		$table = str_replace("</tr><tr>","",$table);
		$table = str_replace("</tr>", "", $table);
		$table = str_replace("</td>","<td>" ,$table);
		$table = str_replace("td width=\"30\"","td" ,$table);
		$table = str_replace("\n" ,"" ,$table);
		$table = str_replace("\t", "" ,$table);
		$table = str_replace(" ", "" ,$table);
		$table = str_replace("<td>","td",$table);
		$table = str_replace("tdtd","td",$table);

		$Array = explode("td" ,$table);

		
		/**
		 *	$Array结果介绍：
		 *	首先
		 *	0 => ""
		 *	1 => "课程名"
		 *	2 => "教师"
		 *  3 => "开课系"
		 *  4 => "学分"
		 *  5 => "课程性质"
		 *  其次
		 *  每个序号mod 6 所得值对应上面的内容
		 * 
		 */
		var_dump($Array);

	}


	public function KaoShiBiao($year ,$term){
		$data = "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwULLTE2NTU5MjUyNDUPZBYCAgEPZBYCAgEPZBYIAgEPZBYCZg9kFgQCAQ8QZBAVDQnor7fpgInmi6kFMjAxNTIFMjAxNTEFMjAxNDIFMjAxNDEFMjAxMzIFMjAxMzEFMjAxMjIFMjAxMjEFMjAxMTIFMjAxMTEFMjAxMDIFMjAxMDEVDQnor7fpgInmi6kFMjAxNTIFMjAxNTEFMjAxNDIFMjAxNDEFMjAxMzIFMjAxMzEFMjAxMjIFMjAxMjEFMjAxMTIFMjAxMTEFMjAxMDIFMjAxMDEUKwMNZ2dnZ2dnZ2dnZ2dnZ2RkAggPEGRkFgFmZAICD2QWAmYPZBYCZg8PFgIeBFRleHRlZGQCAw9kFgJmD2QWBmYPDxYCHwAFEeWtpuWPt%2B%2B8mjEwMTQyMDQ1ZGQCAg8PFgIfAAUS5aeT5ZCN77ya5q%2Bb6LCm5piCZGQCBA8PFgIfAAUZMjAxNS0yMDE25a2m5bm056ysMeWtpuacn2RkAgQPZBYCZg9kFgRmDzwrAAsBAA8WCB4IRGF0YUtleXMWAB4LXyFJdGVtQ291bnQCCR4JUGFnZUNvdW50AgEeFV8hRGF0YVNvdXJjZUl0ZW1Db3VudAIJZBYCZg9kFhICAQ9kFgxmDw8WAh8ABSPogIHlrZDmgJ3mg7PkuI7nvo7lm73miI%2Fliaco5Y%2BM6K%2BtKWRkAgEPDxYCHwAFCjE1MTQwMTgyMDFkZAICDw8WAh8ABQRFNDAxZGQCAw8PFgIfAAUlMjAxNSDlubQxMiDmnIgxNSDml6XmmZrkuIogNjowMC04OjAwIGRkAgQPDxYCHwAFBue7k%2Badn2RkAgUPDxYCHwAFCeWQtOaJv%2BmSp2RkAgIPZBYMZg8PFgIfAAUS5Yqo5oCB572R6aG16K6%2B6K6hZGQCAQ8PFgIfAAUKMTUxNDAxMzEwMWRkAgIPDxYCHwAFBEUzMjFkZAIDDw8WAh8ABSQyMDE1IOW5tDEyIOaciDE3IOaXpeaZmuS4ijU6NTAtNzo1MCBkZAIEDw8WAh8ABQbnu5PmnZ9kZAIFDw8WAh8ABQnorrjljavmnpdkZAIDD2QWDGYPDxYCHwAFDOiQpemUgOeuoeeQhmRkAgEPDxYCHwAFCjE1MTIwMzgyMDNkZAICDw8WAh8ABQRCMTAxZGQCAw8PFgIfAAUkMjAxNiDlubQxIOaciDQg5pel5LiK5Y2IIDk6MzAtMTE6MzAgZGQCBA8PFgIfAAUG57uT5p2fZGQCBQ8PFgIfAAUJ6ZmI5bO75p2%2BZGQCBA9kFgxmDw8WAh8ABRLlpKflraboi7Hor63kuInnuqdkZAIBDw8WAh8ABQoxNTEyMDM4NTAxZGQCAg8PFgIfAAUEQjIwMmRkAgMPDxYCHwAFJDIwMTYg5bm0MSDmnIg1IOaXpeS4iuWNiCA5OjMwLTExOjMwIGRkAgQPDxYCHwAFBue7k%2Badn2RkAgUPDxYCHwAFCeW8oOmDneiOiWRkAgUPZBYMZg8PFgIfAAU75q%2Bb5rO95Lic5oCd5oOz5ZKM5Lit5Zu954m56Imy56S%2B5Lya5Li75LmJ55CG6K665L2T57O7KOS4iilkZAIBDw8WAh8ABQoxNTEyMDAyOTAxZGQCAg8PFgIfAAUEQTIwNWRkAgMPDxYCHwAFIzIwMTYg5bm0MSDmnIg2IOaXpeS4i%2BWNiCAyOjAwLTQ6MDAgZGQCBA8PFgIfAAUG57uT5p2fZGQCBQ8PFgIfAAUG5Yav5YabZGQCBg9kFgxmDw8WAh8ABQ%2FotKLliqHkvJrorqEoSSlkZAIBDw8WAh8ABQoxNTEyMDM4MzAyZGQCAg8PFgIfAAUEQjMwMmRkAgMPDxYCHwAFJDIwMTYg5bm0MSDmnIg3IOaXpeS4iuWNiCA5OjMwLTExOjMwIGRkAgQPDxYCHwAFBue7k%2Badn2RkAgUPDxYCHwAFCemZiOWwj%2BW5s2RkAgcPZBYMZg8PFgIfAAUY5qaC546H6K665LiO5pWw55CG57uf6K6hZGQCAQ8PFgIfAAUKMTUxMjAzODAwMmRkAgIPDxYCHwAFBEExMDRkZAIDDw8WAh8ABSQyMDE2IOW5tDEg5pyIOCDml6XkuIrljYggOTozMC0xMTozMCBkZAIEDw8WAh8ABQbnu5PmnZ9kZAIFDw8WAh8ABQbmuKnmtptkZAIID2QWDGYPDxYCHwAFDOe6v%2BaAp%2BS7o%2BaVsGRkAgEPDxYCHwAFCjE1MTIwMzc5MDJkZAICDw8WAh8ABQRCMTAyZGQCAw8PFgIfAAUlMjAxNiDlubQxIOaciDExIOaXpeS4iuWNiCA5OjMwLTExOjMwIGRkAgQPDxYCHwAFBue7k%2Badn2RkAgUPDxYCHwAFCeeOi%2BWHoeWHoWRkAgkPZBYMZg8PFgIfAAUS55S15a2Q5ZWG5Yqh5qaC6K66ZGQCAQ8PFgIfAAUKMTUxMjAzODEwMWRkAgIPDxYCHwAFBEExMDFkZAIDDw8WAh8ABSQyMDE2IOW5tDEg5pyIMTQg5pel5LiL5Y2IIDI6MDAtNDowMCBkZAIEDw8WAh8ABQbnu5PmnZ9kZAIFDw8WAh8ABQblkajkvJ9kZAICDw8WAh4HVmlzaWJsZWdkZGRy%2FSTkh%2BjBMNiVzVEpk%2FfsCuKeAw%3D%3D&ddlYearTerm=".$year.$term."&btnSelect=%E6%9F%A5%E8%AF%A2&RdbCourse=%E4%B8%AA%E4%BA%BA%E8%80%83%E8%AF%95%E8%A1%A8&__EVENTVALIDATION=%2FwEWEgLai%2BvnBALekp65DQKP%2BokJAoD6iQkCj%2FqdogsCgPqdogsCj%2FrhxgICgPrhxgICj%2Fr1mwoCgPr1mwoCj%2FrZvAUCgPrZvAUCj%2Fqt0QwCgPqt0QwC2sfb1QYCuaHTqAgCj%2FnpnQ4CwZTn4wj2HJgE82CKqJCUCxGEAZ384PkhZQ%3D%3D";
		//真JB长
		$url = "http://202.120.108.14/ecustedu/K_StudentQuery/K_TestTableDetail.aspx";
		$opt = $this->curl_POST($url,$data);

		echo $opt;

		// 又到了切割机上场的时候了
	}
}


// echo $EcustID;
// echo $EcustPW;

$test = new Ecust($EcustID,$EcustPW);


var_dump($test);
//$test->KaoShiBiao(2015,1);

//$test->XuanKeXinXi(2014,1);

//$tset->changePW('woshishabi');