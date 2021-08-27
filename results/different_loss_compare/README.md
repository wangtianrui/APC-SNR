The models trained by our loss function (APC-SNR or PMSQE1+APC-SNR) are the best on the comprehensive performance.

All results are sorted from small to large according to the CI index in our paper.

#### model in paper (NsNET) trained by different loss function.

* (python36) F:\python programes\APC-SNR>python analysis.py model_in_paper
```txt
------------------------------ PMSQE1.csv ------------------------------
       pesq_wb   apc-snr  time_sisnr_  stoi_score  pmsqe_score       mse  \
std   0.885604  3.210944     3.100253    0.079843     0.462479  0.108243
mean  2.819146  6.966474     6.793499    0.915208     0.609486  0.092088

       apc-mse  stft_diff        snr      log_mse      time        CI
std   0.009841   0.035318  11.380700  1672.448470  0.191178 -1.067367
mean  0.010735   0.135234   9.627286  6668.395815  0.174532 -1.067367
------------------------------ STOI.csv ------------------------------
       pesq_wb    apc-snr  time_sisnr_  stoi_score  pmsqe_score       mse  \
std   0.916190   6.309723     7.650743    0.073037     0.727168  0.033223
mean  2.421587  10.702118    14.932098    0.942021     1.128424  0.016135

       apc-mse  stft_diff        snr      log_mse      time        CI
std   0.006644   0.043790  11.380700  1788.278757  0.039769 -0.336705
mean  0.004626   0.102257   9.627286  6154.422389  0.165325 -0.336705
------------------------------ PMSQE.csv ------------------------------
       pesq_wb    apc-snr  time_sisnr_  stoi_score  pmsqe_score       mse  \
std   0.913308   6.797561     8.256733    0.086187     0.638651  0.027477
mean  2.608862  12.282501    15.535787    0.928366     0.913599  0.013817

       apc-mse  stft_diff        snr      log_mse      time        CI
std   0.004799   0.035834  11.380700  1329.387698  0.096284 -0.310001
mean  0.003443   0.087506   9.627286  4717.880032  0.168999 -0.310001
------------------------------ MSE.csv ------------------------------
       pesq_wb    apc-snr  time_sisnr_  stoi_score  pmsqe_score       mse  \
std   0.889027   6.556404     8.005335    0.078473     0.592897  0.021589
mean  2.593183  12.988769    17.098206    0.934021     0.903568  0.010040

       apc-mse  stft_diff        snr      log_mse      time        CI
std   0.004075   0.033662  11.380700  1438.310945  0.023291  0.010275
mean  0.002936   0.089574   9.627286  5136.124110  0.153320  0.010275
------------------------------ SI-SNR.csv ------------------------------
       pesq_wb    apc-snr  time_sisnr_  stoi_score  pmsqe_score       mse  \
std   0.917275   6.697482     8.126247    0.077372     0.631717  0.023851
mean  2.637803  13.079809    17.482367    0.937436     0.918886  0.010669

       apc-mse  stft_diff        snr      log_mse      time        CI
std   0.004219   0.032972  11.380700  1598.195230  0.034394  0.295149
mean  0.002957   0.088835   9.627286  5421.023171  0.154234  0.295149
------------------------------ APC-SNR.csv ------------------------------
       pesq_wb    apc-snr  time_sisnr_  stoi_score  pmsqe_score       mse  \
std   0.925940   6.735696     8.227054    0.077457     0.576913  0.023204
mean  2.717651  13.568513    17.531977    0.938980     0.813688  0.009959

       apc-mse  stft_diff        snr      log_mse      time        CI
std   0.003942   0.033922  11.380700  1463.192586  0.043477  0.570436
mean  0.002709   0.083246   9.627286  5113.331380  0.160313  0.570436
------------------------------ PMSQE1+APC-SNR.csv ------------------------------
       pesq_wb    apc-snr  time_sisnr_  stoi_score  pmsqe_score       mse  \
std   0.939416   6.729692     8.198711    0.075890     0.521013  0.021263
mean  2.794378  13.677221    17.637924    0.940408     0.710305  0.009601

       apc-mse  stft_diff        snr      log_mse      time        CI
std   0.003782   0.033273  11.380700  1476.335639  0.013591  0.838212
mean  0.002642   0.083032   9.627286  5044.413008  0.153787  0.838212
```



#### DCRN trained by different loss function.

> If the mask apply methods of model is different, the action mechanism of loss function will be affected. So it’s another research we will publish soon. We have not shown it in this paper.  

* (python36) F:\python programes\APC-SNR>python analysis.py dcrn

```txt
------------------------------ PMSQE.csv ------------------------------
       pesq_wb   pesq_nb   apc-snr  time_sisnr_  stoi_score  pmsqe_score  \
std   0.722245  0.743013  1.082325     1.134453    0.084694     0.618090
mean  2.285199  2.805140  6.497373     6.507226    0.918010     1.123879

          time       mse      log_mse        CI
std   0.050024  0.852268  1277.142161 -1.335816
mean  0.374750  0.739536  4684.820424 -1.335816
------------------------------ STOI.csv ------------------------------
       pesq_wb   pesq_nb    apc-snr  time_sisnr_  stoi_score  pmsqe_score  \
std   0.902221  0.865075   2.005889     2.267596    0.089532     0.805570
mean  2.141888  2.606973  13.100688    13.693197    0.917886     1.414646

          time       mse      log_mse        CI
std   0.006431  0.802877  1665.579885 -1.107117
mean  0.285633  0.754603  6540.993792 -1.107117
------------------------------ PMSQE1.csv ------------------------------
       pesq_wb   pesq_nb   apc-snr  time_sisnr_  stoi_score  pmsqe_score  \
std   0.871956  0.819457  0.975210     0.956333    0.075617     0.532536
mean  2.670215  3.156578  4.040768     3.952440    0.933617     0.765608

          time       mse      log_mse        CI
std   0.051112  0.886549  1391.272701 -0.409464
mean  0.396556  0.765121  5003.232417 -0.409464
------------------------------ MSE.csv ------------------------------
       pesq_wb   pesq_nb    apc-snr  time_sisnr_  stoi_score  pmsqe_score  \
std   0.869847  0.790393   6.508225     8.000791    0.077054     0.606798
mean  2.622014  3.057390  13.462180    17.338863    0.937252     0.894019

          time       mse      log_mse        CI
std   0.026291  0.018310  1344.922938  0.462829
mean  0.339722  0.008754  5091.116865  0.462829
------------------------------ SI-SNR.csv ------------------------------
       pesq_wb   pesq_nb    apc-snr  time_sisnr_  stoi_score  pmsqe_score  \
std   0.892635  0.797894   6.650916     8.096310    0.075642     0.607811
mean  2.685761  3.116080  13.634782    17.532762    0.939228     0.859444

          time       mse      log_mse        CI
std   0.051400  1.287860  1341.251005  0.633437
mean  0.403344  1.122308  4978.711163  0.633437
------------------------------ PMSQE1+APC-SNR.csv ------------------------------
       pesq_wb   pesq_nb    apc-snr  time_sisnr_  stoi_score  pmsqe_score  \
std   0.917321  0.818154   6.649614     8.109513    0.074625     0.562606
mean  2.777020  3.198914  14.044983    17.706681    0.942018     0.736298

          time       mse      log_mse        CI
std   0.027447  1.283255  1347.922655  0.869978
mean  0.340153  1.114424  4818.440187  0.869978
------------------------------ APC-SNR.csv ------------------------------
       pesq_wb   pesq_nb    apc-snr  time_sisnr_  stoi_score  pmsqe_score  \
std   0.909985  0.809029   6.668091     8.155011    0.074218     0.585604
mean  2.770679  3.189733  14.167096    17.852413    0.942504     0.788317

          time       mse      log_mse        CI
std   0.050741  1.285023  1343.351034  0.886154
mean  0.401119  1.116907  4861.222821  0.886154
```



