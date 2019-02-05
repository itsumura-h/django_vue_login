import Util from './Util';

export default {
  methods: {
    login(email: string, password: string) {
      const url = '/api/login';
      const params = {
        email,
        password,
      };
      return Util.methods.postApi(url, params);
    },
    test(url: string) {
      return Util.methods.getApi(url);
    },
    postTest(url: string, params: {value1: string, value2: string}) {
      return Util.methods.postApiTest(url, params);
    },
  },
};
