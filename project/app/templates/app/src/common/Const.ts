// TypeScriptの文字列定数の管理方法
// https://qiita.com/ConquestArrow/items/494d798a4e0788c41a7c

import * as Cookies from 'js-cookie';

namespace Const {
  let apihost: string;
  let csrftoken: string|undefined;

  if (process.env.NODE_ENV === 'development') {
    apihost = 'http://localhost:8000';
    csrftoken = '';
  } else {
    apihost = window.location.origin;
    csrftoken = Cookies.get('csrftoken');
  }
  export const APIHOST = apihost;
  export const CSRFTOKEN = csrftoken;
}

export default Const;
