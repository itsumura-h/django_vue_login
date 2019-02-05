import axios from 'axios';
import Const from './Const';

export default {
  methods: {
    getApi(url: string): Promise<void> {
      url = Const.APIHOST + url;
      return axios
        .get(url)
        .then((response: any) => {
          return response.data.value;
        })
        .catch((err: any) => {
          console.error(err);
        });
    },
    postApi(url: string, params: any) {
      url = Const.APIHOST + url;
      return axios
        .post(url, params)
        .then((response: any) => {
          return response.data.value;
        })
        .catch((err: any) => {
          console.error(err);
        });
    },
    postApiTest(url: string, params: {value1: string, value2: string}): Promise<void> {
      url = Const.APIHOST + url;
      return axios
        .post(url, params)
        .then((response: any) => {
          return response.data.value;
        })
        .catch((err: any) => {
          console.error(err);
        });
    },
    alert(message: string): void {
      alert(message);
    },
  },
};
