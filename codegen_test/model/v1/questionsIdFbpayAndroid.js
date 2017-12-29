/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdFbpayAndroid = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            bonus   'integer' 
            order_type   'string' 订单类型 提问/偷听/赞赏
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/fbpay/android",
            method: "POST",
            data: {
                bonus: obj.bonus,
                order_type: obj.order_type
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    QuestionsIdFbpayAndroid: new QuestionsIdFbpayAndroid
};