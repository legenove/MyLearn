/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdPay = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            bonus   'integer' 
            trade_type   'string' 
            order_type   'string' 订单类型 提问/偷听/赞赏
            
        @success
            status 201    type:object
            trade_type   'string' 
            prepay_id   'string' 
            nonce_str   'string' 
            return_code   'string' 
            return_msg   'string' 错误原因
            sign   'string' 
            device_info   'string' 
            mch_type   'string' 
            err_code_des   'string' 
            appid   'string' 
            time_stamp   'string' 
            mweb_url   'string' 
            code_url   'string' trade_type为NATIVE是有返回
            result_code   'string' 业务结果
            err_code   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/pay",
            method: "POST",
            data: {
                bonus: obj.bonus,
                trade_type: obj.trade_type || "NATIVE",
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
    QuestionsIdPay: new QuestionsIdPay
};