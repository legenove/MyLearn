/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var WeixinPay = function () {
    /*
        @params obj 'data params'
            trade_type   'string' 
            target_id   'string' 
            order_type   'string' 订单类型 提问/偷听/赞赏/悬赏/小讲/小讲礼物/小讲合辑
            target_type   'string' 
            
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
            url: "/weixin/pay",
            method: "POST",
            data: {
                trade_type: obj.trade_type || "NATIVE",
                target_id: obj.target_id,
                order_type: obj.order_type,
                target_type: obj.target_type
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
    WeixinPay: new WeixinPay
};