<?php
date_default_timezone_get("Asia/Chongqing");
$EcustID = $_GET['id'];
$EcustPW = $_GET['pw'];

class loginEcust{
	public $curlobj;
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

	public function curl_GET($url,$data){
		//没用到Get先不写
	}

	public function changePW($newPW){
		// if ($this->success == true){
		// 	return 0;
		// }else{
			$data = "__VIEWSTATE=%2FwEPDwUKMTYzMjI1NzMyN2Rk6a%2BHx5mRWLuy0dJqc2wHB2274JE%3D&txtNewPwd1=".$newPW."&txtNewPwd2=".$newPW."&BtnOK=%E6%8F%90%E4%BA%A4&__EVENTVALIDATION=%2FwEWBAKll4qhCgL7mJ6BBAL7mJqBBAL9mpmPAVpXeLI7SJ4Gqk%2BqA%2BCwBw1nWJFC";
			$url = "http://202.120.108.14/ecustedu/StudentChangePassword.aspx";
			$this->curl_POST($url,$data);
			
			//return 1;
		// }
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
			//通过正则截取数据（官网太丑= =
			echo $opt;
	}
}
